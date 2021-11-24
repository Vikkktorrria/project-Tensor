

export const authModule = {
    state: () => ({
        isAuth: false
    }),
    mutations: {
        setAuth(state, auth) {
            state.isAuth = auth;
        },
    },
    namespaced:true,
}