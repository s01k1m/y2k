import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/LoginView.vue'
import Stills from '../views/StillsView.vue'
import Create from '../views/CreateView.vue'
import Signup from '../views/SignUpView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Stills',
    component: Stills
  },
  {
    path: '/create',
    name: 'Create',
    component: Create
  },
  {
    path: '/login',
    name: 'accounts',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
