import Vue from "vue";
import Vuex from "vuex";
import router from "../router";
import axios from "axios";

// const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex);
export default new Vuex.Store({
//data 옵션의 기본 상태(state) 정의
  state: {
    userInfo: null, //아직 정보를 받아오지 않은 상태이므로 null
    isLogin: false, //로그인이 되었다면 true로 변경
    isLoginError: false,
    token: null,
  }, 
  mutations: {
    loginSuccess(state, payload) { //로그인 성공시,
      console.log('loginSuccess')
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
      localStorage.setItem('username', state.userInfo.username)


      //payload 에 대한 정보는 위키피디아를 참고했다. 쉽게 말해 userInfo에 배정되는 실제 유저 정보를 할당한다고 보면 된다. 
    },
    loginError(state) { //로그인 실패시,
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state) { //로그 아웃시,
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
      state.token = null;
      localStorage.removeItem('access_token')
      localStorage.removeItem('username')
    },

    /////////// signup & login -> 완료하면 토큰 발급 ////////
    SAVE_TOKEN(state, token) {
      console.log('SAVE_TOKEN: ',token)
      state.token = token
      console.log(state.token)
      router.push({ name: "home" }); // store/index.js $router 접근 불가 -> import를 해야함
    },
  },
  actions : {

    /////////로그인/////////
    login(dispatch, loginObj) {
    // login --> 토큰 반환
      axios
      .post("http://127.0.0.1:8000/accounts/login/", loginObj)
      // loginObj = {email,password}를 받아온다.
      .then(res => {
        // 접근 성공시, 토큰 값이 반환된다. (실제로는 토큰과 함께 유저 id를 받아온다.)
        // 토큰을 헤더 정보에 포함시켜서 유저 정보를 요청
        let token = res.data.key
        //토큰을 로컬 스토리지에 저장
        localStorage.setItem('access_token', token)
        // let refretoken = res.data.refresh_token
        // console.log('refretoken',res.data.refresh_token)
        // localStorage.setItem('refresh_token', refretoken)
        
        this.dispatch("getMemberInfo");
        this.commit('SAVE_TOKEN', token)
      })  
      .catch(() => {
        alert("로그인 실패 : 이메일과 비밀번호를 확인하세요.");
      })
    },
    
    /////////로그아웃/////////
    logout({ commit }) {
      commit("logout");
      router.push({ name: "home" });
    },
    
    /////////회원가입/////////
    signup(dispatch, loginObj) {
      // login --> 토큰 반환
      axios
        .post("http://127.0.0.1:8000/accounts/signup/", loginObj)
        // loginObj = {email,password}
        .then(res => {
          alert("회원가입이 성공적으로 이뤄졌습니다.");
          router.push({ name: "login" })
          console.log(res)
        })
        .catch(() => {
          alert("회원가입 실패 : 이메일과 비밀번호를 확인하세요.");
        })
    },
    
    /////////사용자 정보 가져오기/////////
    getMemberInfo({ commit }) {
      console.log('getMeberInfo')
      //로컬 스토리지에 저장된 토큰을 저장한다.
      let token = localStorage.getItem("access_token")
      let config = {
        headers: {
          Authorization: 'Token ' + token
        }
      }
      // 로그인 체크 안하고 싶은 URL
      let except_url = new Array('http://localhost:8080/')
      let current_url = window.location.href

      if (except_url.includes(current_url)){
        console.log("지금 페이지는", current_url, "로그인 검사를 안 합니다."
        )
        return 
      } else {
        //토큰 -> 멤버 정보 반환
        //새로고침 --> 토큰만 갖고 멤버 정보 요청가능
        axios
        .get("http://127.0.0.1:8000/accounts/user/", config)
        .then(response => {
          console.log('getMemberInfo then')
          let userInfo = {
            pk: response.data.pk,
            username: response.data.username,
            email: response.data.email
          }
          commit("loginSuccess", userInfo)
        })
        .catch(() => {
          alert("사용자 정보를 가져오는데 실패 : 이메일과 비밀번호를 확인하세요.");
        });
      }
      },
  },
  getters: {
    getUserName (state) {
      return state.userInfo.username
    }
  }
});