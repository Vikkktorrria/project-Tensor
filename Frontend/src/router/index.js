import Registration from "../pages/Registration";
import {createRouter, createWebHistory} from "vue-router";
import Auth from "../pages/Auth";
import Question from "../pages/Question";


const routes = [
    {
        path: '/registration',
        component: Registration
    },
    {
        path: '/auth',
        component: Auth
    },
    {
        path: '/question',
        component: Question
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;