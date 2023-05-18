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
    isLoginError: false
    },
    
  mutations: {
      loginSuccess(state, payload) { //로그인 성공시,
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
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
      },
      /////////// signup & login -> 완료하면 토큰 발급 ////////
      SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $router 접근 불가 -> import를 해야함
      }
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
    let token = res.data.token;
    //토큰을 로컬 스토리지에 저장
    localStorage.setItem("access_token", token); //로컬 스토리지에 토큰 저장
    this.dispatch("getMemberInfo");
    router.push({ name: "home" });
    console.log(res);
    })
    .catch(() => {
    alert("이메일과 비밀번호를 확인하세요.");
    });
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
    router.push({ name: "login" });
    console.log(res);
    })
    .catch(() => {
    alert("이메일과 비밀번호를 확인하세요.");
    });
    },
    
    /////////사용자 정보 가져오기/////////
    getMemberInfo({ commit }) {
    //로컬 스토리지에 저장된 토큰을 저장한다.
    let token = localStorage.getItem("access_token");
    let config = {
    headers: {
    "access-token": token
    }
    };
    //토큰 -> 멤버 정보 반환
    //새로고침 --> 토큰만 갖고 멤버 정보 요청가능
    axios
    .get("http://127.0.0.1:8000/accounts/user/", config)
    .then(response => {
    let userInfo = {
    pk: response.data.data.pk,
    username: response.data.data.username,
    email: response.data.data.email
    };
    commit("loginSuccess", userInfo);
    })
    .catch(() => {
    alert("이메일과 비밀번호를 확인하세요.");
    });
    }
  }
});