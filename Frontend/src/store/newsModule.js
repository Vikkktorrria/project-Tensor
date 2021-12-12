import axios from "axios";


export const newsModule = {
    state: () => ({
        news: [],
    }),
    mutations: {
        setNews(state, news) {
            state.news = news;
        }
    },
    actions: {
        async fetchNews({state, commit}) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/news')
                let news = response.data
                news = news.sort((a,b) => {
                    return new Date(b.created_on) - new Date(a.created_on);
                });
                news.forEach((el) => {
                    let created_on = el.created_on.split('T')[0]
                    created_on = created_on.split('-')
                    let day = created_on[2]
                    let month = created_on[1]
                    let year = created_on[0]
                    if (day.split('')[0] === '0') {
                        day = day.split('')[1]
                    }
                    if (month.split('')[0] === '0') {
                        day = month.split('')[1]
                    }
                    el.created_on = day + '.' + month + '.' + year
                })
                commit('setNews', news)
            } catch (e) {
                console.log(e)
            }
        },
    },
    namespaced:true,
}