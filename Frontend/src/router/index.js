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
import ProfileDoctor from "../pages/ProfileDoctor";
import Error from "../pages/Error";
import store from "../store/index"


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
        path: '/profile-doctor',
        name: 'profile-doctor',
        component: ProfileDoctor
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
    },
    {
        path: "/:catchAll(.*)",
        name: "NotFound",
        component: Error
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})
const isAuthenticated = () => false;

router.beforeEach((to, from, next) => {
    if (to.matched.some((route) => route.name === 'auth' || route.name === 'registration' || route.name === 'startPage' || route.name === 'question') || store.getters["auth/getAuth"]) {
        next();
    } else {
        next("/auth");
    }
});
export default router;