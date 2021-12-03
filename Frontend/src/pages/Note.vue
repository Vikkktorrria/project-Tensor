<template>
  <h1 class="h1-text">Запись</h1>
  <p
      class="h1-text"
      style="font-size: 25px"
      v-if="!currentUser.isDoctor"
  >Выберите время записи</p>
  <my-dialog v-model:show="dialogVisible">
    <create-note
        @create="setTextNote"
    ></create-note>
  </my-dialog>
  <my-dialog v-model:show="dialogUpdateVisible">
    <update-note
        :note="currentNote"
        @create="updateNote"
    ></update-note>
  </my-dialog>
  <FullCalendar
      ref="fullCalendar"
      :options="calendarOptions"
  />
</template>

<script>
import '@fullcalendar/core/vdom'
import FullCalendar from '@fullcalendar/vue3'
import CreateNote from "../components/CreateNote";
import UpdateNote from "../components/UpdateNote";
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid';
import ruLocale from "@fullcalendar/core/locales/ru";
import interactionPlugin from '@fullcalendar/interaction'
import axios from "axios";
import {mapState} from "vuex";

let eventGuid = 0
let selInfo;
export default {
  name: "Note",
  data() {
    return {
      dialogVisible: false,
      textNote: '',
      calendarOptions: {
        locale: ruLocale,
        plugins: [
          dayGridPlugin,
          timeGridPlugin,
          interactionPlugin
        ],
        headerToolbar: {
          left: 'timeGridWeek,timeGridDay',
          center: 'title',
          right: 'today prev,next'
        },
        dateClick: (e) => {
          //handle date click
        },
        businessHours: [
          {
            daysOfWeek: [1, 2, 3, 4, 5],
            startTime: '8:00',
            endTime: '18:00',
          }
        ],
        events: null,
        /* you can update a remote database when these fire:
        eventAdd:
        eventChange:
        eventRemove:
        */
        initialView: 'timeGridWeek',
        initialEvents: this.startEvents, // alternatively, use the `events` setting to fetch from a feed
        editable: false,
        selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        weekends: false,
        select: this.handleDateSelect,
        eventClick: this.handleEventClick,
        eventsSet: this.handleEvents
      },
      startEvents: [],
      currentEvents: [],
      currentNote: [],
      dialogUpdateVisible: false
    }
  },
  methods: {
    async setTextNote(doctor) {
      this.dialogVisible = false;
      let counter = 0
      this.currentEvents.forEach((el) => {
        if (el.extendedProps.userId === this.currentUser.id && el.start > Date.now()) {
          counter += 1
        }
      })
      if (counter > 4) {
        alert('Вы создали более 4-х записей')
      } else {
        this.textNote = `${doctor.fullName.surname}  ${doctor.fullName.name}`
        let title = this.textNote
        let selectInfo = selInfo
        let calendarApi = selectInfo.view.calendar
        calendarApi.addEvent({
          id: this.createEventId(),
          title: 'Доктор: ' + title,
          start: selectInfo.startStr,
          end: selectInfo.endStr,
          allDay: selectInfo.allDay
        })
        try {
          this.currentEvents = [
            ...this.currentEvents,
            selectInfo
          ]
          const response = await axios.post('http://127.0.0.1:5000/api/user/patient/note', {
            date_of_visit: selectInfo.startStr,
            doctor_id: doctor.id
          }, {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
            'Content-type': 'application/json'
          })
          console.log(response)
        } catch (error) {
          alert(error.request.response)
        } finally {

        }
      }
      // await this.fetchNotes()
    },
    updateNote() {
      this.dialogUpdateVisible = false;
    },
    createEventId() {
      return String(eventGuid++)
    },
    handleWeekendsToggle() {
      this.calendarOptions.weekends = !this.calendarOptions.weekends // update a property
    },
    handleDateSelect(selectInfo) {
      let calendarApi = selectInfo.view.calendar
      if (selectInfo.start < new Date()) {
        alert('Выбранное время уже прошло')
        calendarApi.unselect()
      } else if (selectInfo.start.getHours() < 8 || selectInfo.start.getHours() > 17) {
        alert('В это время больница не работает')
        calendarApi.unselect()
      } else {
        this.dialogVisible = true
        selInfo = selectInfo
      }
    },
    async handleEventClick(clickInfo) {
      if (this.currentUser.isDoctor) {
        this.currentNote = clickInfo.event.extendedProps.note
        this.dialogUpdateVisible = true
      } else if (Number(clickInfo.event.extendedProps.userId) !== Number(this.$store.state.auth.currentUser.id)) {
        alert('Это не ваша запись')
      } else if (confirm(`Вы уверены, что хотите удалить событие '${clickInfo.event.title}'`)) {
        clickInfo.event.remove()
        try {
          const response = await axios.delete(`http://127.0.0.1:5000/api/user/patient/delete/note/${clickInfo.event.id}`, {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}
          })
          console.log(response)
        } catch (error) {
          alert(error.request.response)
        } finally {

        }
      }
    },
    handleEvents(events) {
      this.currentEvents = events
    },
    async fetchNotes(e) {
      let calendarApi = this.$refs.fullCalendar.getApi()
      let result
      if (this.currentUser.isDoctor) {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/user/doctor/note', {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
          result = response.data
          result.forEach((item) => {
            let timeEnd = new Date((Date.parse(item['date_of_visit']) + 3600000 / 2))
            calendarApi.addEvent({
              id: item.id,
              title: 'Пациент: ' + item.patient.surname + ' ' + item.patient.name + ' ' + item.patient.patronymic,
              start: item['date_of_visit'],
              editable: false,
              end: timeEnd,
              extendedProps: {
                note: item,
                userId: item['user_id']
              }
            })
          })
        } catch (error) {
          alert(error.request.response)
        } finally {

        }
      } else {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/diagnoses', {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
          result = response.data
          result.forEach((item) => {
            let timeEnd = new Date((Date.parse(item['date_of_visit']) + 3600000 / 2))
            calendarApi.addEvent({
              id: item.id,
              title: 'Доктор: ' + item.doctor.surname + " " + item.doctor.name,
              start: item['date_of_visit'],
              editable: false,
              end: timeEnd,
              extendedProps: {
                userId: item['user_id']
              }
            })
          })
        } catch (error) {
          alert(error.request.response)
        } finally {

        }
      }
    },
  },
  components: {
    FullCalendar,
    CreateNote,
    UpdateNote
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
    })
  },
  mounted() {
    this.fetchNotes()
  }
}
</script>

<style>
.fc .fc-toolbar-title {
  font-size: 1.75em;
  margin: 0;
  font-family: 'Roboto-light';
  color: #35538d;
}

.fc .fc-button-primary {
  color: #ffffff;
  background-color: #8cbaf7;
  border-color: #8cbaf7;
}

.fc .fc-button-primary:hover {
  color: #fff;
  background-color: #589cf7;
  border-color: #589cf7;
}

.fc .fc-button-primary:disabled {
  color: #fff;
  background-color: #b5d3f3;
  border-color: #b5d3f3;
}

.fc .fc-button-primary:focus {
  box-shadow: 0 0 0 0.2rem rgba(11, 127, 252, 0.5);
}

.fc .fc-button-primary:not(:disabled):active,
.fc .fc-button-primary:not(:disabled).fc-button-active {
  color: #fff;
  background-color: #2e73ce;
  border-color: #2e73ce;
}

.fc .fc-button-primary:not(:disabled):active:focus,
.fc .fc-button-primary:not(:disabled).fc-button-active:focus {
  box-shadow: 0 0 0 0.2rem rgba(11, 127, 252, 0.5);
}
</style>