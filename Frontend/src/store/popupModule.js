import axios from "axios";


export const popupModule = {
    state: () => ({
        isPopup: false,
    }),
    mutations: {
        setAuth(state, auth) {
            state.isAuth = auth;
        },
    },
    actions: {
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