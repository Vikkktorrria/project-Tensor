import Registration from "../pages/Registration";
import {createRouter, createWebHistory} from "vue-router";
import Auth from "../pages/Auth";
import Question from "../pages/Question";
import Notification from "../pages/Notification";
import Settings from "../pages/Settings";
import Profile from "../pages/Profile";


const routes = [
    {
        path: '/registration',
        name: 'registration',
        component: Registration
    },
    {
        path: '/auth',
        name: 'auth',
        component: Auth
    },
    {
        path: '/question',
        name: 'question',
        component: Question
    },
    {
        path: '/notification',
        name: 'notification',
        component: Notification
    },,
    {
        path: '/profile',
        name: 'profile',
        component: Profile
    },
    {
        path: '/settings',
        name: 'settings',
        component: Settings
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;