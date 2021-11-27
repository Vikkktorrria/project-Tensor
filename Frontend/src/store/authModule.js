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
        setUser(state, user) {
            const currentTime = new Date()
            const birthDay = new Date(user.b_date)
            const age = Math.floor(((currentTime - birthDay) / (60 * 60 * 24 * 1000)) / 365);
            state.currentUser = {
                name: user.name,
                age: age,
            };
        },
    },
    actions: {
        async userData({state, commit}) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/user/info',  {
                    headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
                })
                commit('setUser', response.data)
            } catch (error) {
                console.log(error.response)
                alert(error.response.data)
            } finally {
            }
        },
    },
    namespaced:true,
}