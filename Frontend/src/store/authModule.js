

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
    namespaced:true,
}