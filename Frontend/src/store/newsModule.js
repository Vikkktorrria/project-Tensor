import axios from "axios";


export const newsModule = {
    state: () => ({
        news: [],
    }),
    mutations: {
        setNews(state, news) {
            state.news = news;
        },
    },
    actions: {
        async fetchNews(e) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/news')
                console.log(response)
                this.news = [...this.news, ...response.data]
            } catch (error) {
                alert(error.request.response)
            } finally {

            }
        },
    },
    namespaced:true,
}