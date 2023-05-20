<template>
  <div class="create">
    <h1>스틸컷을 크리에이트하는 포스팅 페이지입니다. ^^</h1>
    <form>
      <v-file-input
        v-model="files"
        :multiple="false"
        label="File input"
      ></v-file-input>
      <input v-model="searchQuery" @input="getMovies" />
      <div v-if="movies.length === 0">Loading movies...</div>
      <div v-else>
        <!-- <GetMovieData v-for="m in movies" :key="m.id" :movie="m"></GetMovieData> -->
        <div v-for="movie in movies" :key="movie.id">
          <input
            type="radio"
            name="myMovie"
            @click="confirm"
            :id="movie.id"
            :value="movie.movie_title"
          />
          <label :for="movie.id"
            >{{ movie.movie_title }} : {{ movie.id }}</label
          >
        </div>
      </div>

      <br />
      <button @click="sendImages">submit</button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
import FormData from "form-data";
// import GetMovieData from '../components/GetMovieData.vue'

export default {
  name: "CreateView",
  data() {
    return {
      files: null,
      searchQuery: "",
      movies: [],
      movie_id: "",
    };
  },
  component: {
    // GetMovieData,
  },
  props: ["movie"],
  computed: {
    isLogin() {
      return localStorage.getItem("access_token");
    },
  },
  created() {
    this.isLogined();
  },
  methods: {
    // 로그인이 되어있지 않으면 create에 접근할 수 없다.
    isLogined() {
      if (!this.isLogin) {
        console.log("if");
        alert("로그인이 필요합니다.");
        this.$router.push({ name: "login" });
      } else {
        if (!this.$store.state.token) {
          this.$store.dispatch("getMemberInfo");
        }
      }
    },
    // 스틸컷에 해당하는 영화정보 가져오기
    getMovies() {
      const encodedQuery = encodeURIComponent(this.searchQuery);
      axios
        .get(`http://127.0.0.1:8000/create/getmovie/${encodedQuery}`)
        .then((response) => {
          this.movies = response.data;
          console.log("response.data", response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 스틸컷의 영화정보를 검색하여 클릭합니다.
    confirm(e) {
      console.log("클릭한 영화의 id : ", e.target.id);
      this.movie_id = e.target.id;
      console.log("폼으로 최종 제출될 영화의 id : ", this.movie_id);
    },
    // 스틸컷을 최종 제출
    sendImages(e) {
      e.preventDefault(); // 폼 새로 고침 방지
      if (!this.movie_id) {
        alert(
          "스틸컷의 영화 이름을 검색해서 선택하세요. 선택하기 전에는 제출할 수 없습니다."
        );
      } else {
        const form = new FormData();
        form.append("still_image", this.files);
        form.append("movie_id", this.movie_id);
        let token = localStorage.getItem("access_token");
        axios
          .post("http://127.0.0.1:8000/create/", form, {
            headers: {
              "Content-Type": "multipart/form-data",
              // 와 이거 하나땜에 몇시간을 ^0^ 하하하핳ㅋㅋㅋㅋ
              Authorization: "Token " + token,
            },
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (response) {
            //handle error
            console.log(response);
          });
      }
    },
  },
};
</script>

<style scoped>
#create {
  margin: 24px;
}

form {
  width: 400px;
  margin: 0 auto;
}
</style>

input[name="myMovie"]:checked  + label{
  background-color: #333;
  color: #fff;

}