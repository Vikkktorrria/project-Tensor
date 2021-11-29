<template>
  <h1 class="h1-text">Запись</h1>
  <FullCalendar :options="calendarOptions" />
  <div id='calendar'></div>
</template>

<script>
import '@fullcalendar/core/vdom'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
export default {
  name: "Note",
  data() {
    return {
      calendarOptions: {
        plugins: [ dayGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth'
      }
    }
  },
  components: {
    FullCalendar
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
  border-color: #2e73ce ;
}
.fc .fc-button-primary:not(:disabled):active:focus,
.fc .fc-button-primary:not(:disabled).fc-button-active:focus {
  box-shadow: 0 0 0 0.2rem rgba(11, 127, 252, 0.5) ;
}
</style>