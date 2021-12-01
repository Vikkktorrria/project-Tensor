import {createStore} from "vuex";
import {authModule} from "./authModule";
import {newsModule} from "./newsModule";
import {popupModule} from "./popupModule";


export default createStore({
    modules: {
        auth: authModule,
        news: newsModule,
        popup: popupModule
    }
})