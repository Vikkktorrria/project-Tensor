import Registration from "../pages/Registration";
import {createRouter, createWebHistory} from "vue-router";
import Auth from "../pages/Auth";
import Question from "../pages/Question";
import Notification from "../pages/Notification";
import Settings from "../pages/Settings";
import Profile from "../pages/Profile";
import Health from "../pages/Health";
import News from "../pages/News";
import Note from "../pages/Note";


const routes = [
    {
        path: '/',
        name: 'startPage',
        component: News
    },
    {
        path: '/news',
        name: 'news',
        component: News
    },
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
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile
    },
    {
        path: '/health',
        name: 'health',
        component: Health
    },
    {
        path: '/note',
        name: 'note',
        component: Note
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