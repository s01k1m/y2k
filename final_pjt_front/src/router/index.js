import Vue from 'vue'
import VueRouter from 'vue-router'

import Intro from '../views/IntroView.vue'
import Home from '../views/HomeView.vue'
import Search from '../views/SearchView.vue'
import Create from '../views/CreateView.vue'
import LogIn from '../views/LogInView.vue'
import SignUp from '../views/SignUpView.vue'
import User from '../views/UserView.vue'
import Collection from '../views/CollectionView.vue'
import MovieDetail from '../components/MovieDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'intro',
    component: Intro
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/home/:stillId',
    name: 'detail',
    component: MovieDetail
  },
  {
    path: '/stills',
    name: 'collection',
    component: Collection
  },
  {
    path: '/search/:searchInput',
    name: 'search',
    component: Search,
    // true로 설정하면 데이터를 PROPS로 받는다.
    props: true
  },
  {
    path: '/create',
    name: 'create',
    component: Create
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
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
