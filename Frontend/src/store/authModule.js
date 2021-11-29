import axios from "axios";


export const authModule = {
    state: () => ({
        isAuth: false,
        currentUser: [],
    }),
    mutations: {
        setAuth(state, auth) {
            state.isAuth = auth;
        },
        setUser(state, person) {
            if (!person)
                state.currentUser = []
            let user = person.user
            const currentTime = new Date()
            const birthDay = new Date(user.b_date)
            const age = Math.floor(((currentTime - birthDay) / (60 * 60 * 24 * 1000)) / 365);
            let txt;
            let count = age % 100;
            if (count >= 5 && count <= 20) {
                txt = 'лет';
            } else {
                count = count % 10;
                if (count === 1) {
                    txt = 'год';
                } else if (count >= 2 && count <= 4) {
                    txt = 'года';
                } else {
                    txt = 'лет';
                }
            }
            state.currentUser = {
                name: user.name,
                surname: user.surname,
                patronymic: user.patronymic ?? '',
                age: age,
                email: user.mail,
                phone: user.phone_number,
                avatarName: user.avatar_img ?? '',
                ageText: txt,
                publicId: user.public_id,
                passport: {
                    number: person.passport.number ?? '',
                    series: person.passport.series ?? '',
                },
                snils: person.snils ?? '',
                anamnesis: person.anamnesis ?? ''
            };
        },
        // setUserAuth(state, user) {
        //     const currentTime = new Date()
        //     const birthDay = new Date(user.b_date)
        //     const age = Math.floor(((currentTime - birthDay) / (60 * 60 * 24 * 1000)) / 365);
        //     let txt;
        //     let count = age % 100;
        //     if (count >= 5 && count <= 20) {
        //         txt = 'лет';
        //     } else {
        //         count = count % 10;
        //         if (count === 1) {
        //             txt = 'год';
        //         } else if (count >= 2 && count <= 4) {
        //             txt = 'года';
        //         } else {
        //             txt = 'лет';
        //         }
        //     }
        //     state.currentUser = {
        //         name: user.name,
        //         surname: user.surname,
        //         patronymic: user.patronymic ?? '',
        //         age: age,
        //         email: user.mail,
        //         phone: user.phone_number,
        //         avatarName: user.avatar_img ?? '',
        //         ageText: txt,
        //         publicId: user.public_id,
        //     };
        // },
    },
    actions: {
        // async userData({state, commit}) {
        //     try {
        //         const response = await axios.get('http://127.0.0.1:5000/api/user/info',  {
        //             headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
        //         })
        //         commit('setUser', response.data)
        //         console.log(response.data)
        //     } catch (error) {
        //         console.log(error)
        //         alert('Проблема авторизации')
        //         if (!this.isAuth)
        //             this.$router.push({ name: 'notification' });
        //     } finally {
        //     }
        // },
        async checkAuth({state, commit}) {
            if(localStorage.getItem('token')) {
                commit('setAuth', true)
                try {
                    const response = await axios.get('http://127.0.0.1:5000/api/user/info',  {
                        headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
                    })
                    commit('setUser', response.data)
                    console.log(response.data)
                } catch (error) {
                    console.log(error)
                    alert('Проблема авторизации')
                } finally {
                }
            } else {
                commit('setAuth', false)
                commit('setUser', false)
            }
        }
    },
    namespaced:true,
}