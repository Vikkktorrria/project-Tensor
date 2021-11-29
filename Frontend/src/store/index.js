import {createStore} from "vuex";
import {authModule} from "./authModule";
import {newsModule} from "./newsModule";


export default createStore({
    modules: {
        auth: authModule,
        news: newsModule
    }
})