import Vue from 'vue'
import VueRouter from 'vue-router'
<<<<<<< HEAD
import Home from '../views/HomeView.vue'
import Search from '../views/SearchView.vue'
=======


import Login from '../views/LoginView.vue'
import Home from '../views/HomeView.vue'
// import Still from '../views/StillsView.vue'
>>>>>>> 85da6e359ae9438945b0ff39679f1196c81bddcc
import Create from '../views/CreateView.vue'
import Login from '../views/LoginView.vue'
import SignUp from '../views/SignUpView.vue'
import User from '../views/UserView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/create',
    name: 'create',
    component: Create
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/user',
    name: 'user',
    component: User
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
