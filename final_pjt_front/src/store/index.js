import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: [
    ],
  },
  getters: {
  },
  mutations: {
    DO_LOGIN(state, login) {
      state.login = login
    }
  },
  actions: {
    doLogin(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/`,
      })
        .then((res) => {
          context.commit('DO_LOGIN', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
