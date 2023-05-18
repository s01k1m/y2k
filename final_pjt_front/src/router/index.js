import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/HomeView.vue'
import Search from '../views/SearchView.vue'
import Create from '../views/CreateView.vue'
import Login from '../views/LoginView.vue'
import SignUp from '../views/SignUpView.vue'
import User from '../views/UserView.vue'
import Collection from '../views/CollectionView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/stills',
    name: 'collection',
    component: Collection
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
