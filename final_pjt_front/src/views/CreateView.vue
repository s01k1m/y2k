<template>
  <div class="create">
    <h1 id="header">Create your STILL</h1>
    <p>
      Pick your STILL Image file.<br />
      Then, search and pick a movie for it.<br />And submit!
    </p>

    <form>
      <v-file-input
        v-model="files"
        name="still_image"
        :multiple="false"
        label="Find STILL"
        accept="image/png, image/jpeg, image/jpg, image/gif"
      ></v-file-input>
      <v-text-field
        v-model="searchQuery"
        id="getMovies"
        prepend-icon="mdi-magnify"
        label="Find Movie"
        @input="getMovies"
      />
      <div class="form-wrapper">
        <div v-if="movies.length === 0">Loading movies...</div>
        <div
          v-else
          style="background-color: #e9e9e9; border-radius: 30px; padding: 30px"
        >
          <div v-for="movie in movies" :key="movie.id" id="forGetMovies">
            <input
              type="radio"
              name="myMovie"
              @click="confirm"
              :id="movie.id"
              :value="movie.movie_title"
              class="radio-button"
            />
            <label :for="movie.id" class="radio-label"
              >{{ movie.movie_title }} : {{ movie.id }}</label
            >
          </div>
        </div>

        <br />
      </div>
      <v-btn @click="sendImages" class="stillSubmit">submit</v-btn>
      <br />
      <br />
      <br />
      <p class="sorry">
        It may take a moment for your submission to be saved. <br>
        Please wait patiently. <br>
        Thank you for your understanding!
      </p>
      <br />
      <br />
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
  methods: {
    // 스틸컷에 해당하는 영화정보 가져오기
    getMovies() {
      const encodedQuery = encodeURIComponent(this.searchQuery);
      axios
        .get(`http://127.0.0.1:8000/create/getmovie/${encodedQuery}`)
        .then((response) => {
          this.movies = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    // 스틸컷의 영화정보를 검색하여 클릭합니다.
    confirm(e) {
      console.log("클릭한 영화의 id : ", e.target.id)
      this.movie_id = e.target.id
      console.log("폼으로 최종 제출될 영화의 id : ", this.movie_id)
    },
    // 스틸컷을 최종 제출
    sendImages(e) {
      e.preventDefault() // 폼 새로 고침 방지
      if (!this.files) {
        alert(
          "스틸컷 이미지를 업로드 하세요. 업로드 전에는 제출할 수 없습니다."
        );
      } else if (!this.movie_id) {
        alert(
          "스틸컷의 영화 이름을 검색해서 선택하세요. 선택하기 전에는 제출할 수 없습니다."
        );
      } else {
        const form = new FormData();
        form.append("still_image", this.files)
        form.append("movie_id", this.movie_id)
        let token = localStorage.getItem("access_token")
        axios
          .post("http://127.0.0.1:8000/create/", form, {
            headers: {
              "Content-Type": "multipart/form-data",
              // 와 이거 하나땜에 몇시간을 ^0^ 하하하핳ㅋㅋㅋㅋ
              Authorization: "Token " + token,
            },
          })
          .then((response) => {
            console.log('제출 성공!', response);
            alert("정상적으로 제출되었습니다.");
            this.$router.push({name: 'home'})
          })
          .catch(function (err) {
            //handle error
            console.log(err);
          });
      }
    },
  },
};
</script>

<style scoped>
#header {
  margin-top: 50px;
}

#create {
  margin: 24px;
}
h1 {
  margin-bottom: 20px;
}
form {
  width: 400px;
  margin: 0 auto;
}

/* getMovies */
.form-wrapper {
  max-height: 400px; /* Adjust the value as needed */
  overflow-y: auto;
  margin-bottom: 20px; /* Add margin to create space between form and submit button */
  -ms-overflow-style: none; /* 인터넷 익스플로러 */
  scrollbar-width: none; /* 파이어폭스 */
}

/* ( 크롬, 사파리, 오페라, 엣지 ) 동작 */
.form-wrapper::-webkit-scrollbar {
  display: none;
}

#forGetMovies {
  display: flex;
  margin: 10px 0;
  text-align: left;
}
.radio-button {
  appearance: none;
  width: 16px;
  height: 16px;
  border: 2px solid #000;
  border-radius: 50%;
  outline: none;
  margin-right: 10px;
  cursor: pointer;
  margin-top: 4px;
  flex-shrink: 0;
}

.radio-button:checked {
  background-color: #000;
}

.radio-label {
  color: rgba(0, 0, 0, 0.6);
}

.radio-label:hover {
  color: rgb(0, 0, 0);
}

/* 체크된 라디오 버튼 라벨에 대한 스타일링 */
.radio-button:checked + .radio-label {
  font-weight: bold;
  color: rgb(0, 0, 0);
}

/* 최종 제출 버튼 */

button.stillSubmit {
  position: relative;
  background: #ffffff;
  border: 0;
  padding: 14px 42px;
  border-radius: 30px;
  cursor: pointer;
  overflow: hidden;
  outline: none;
  font-weight: 400;
  font-size: 12px;
  color: #000000;
  letter-spacing: 0.2em;
  /* box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2); */
  /* transition: all 0.2s ease; */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 수정된 부분 */
}

button.stillSubmit:hover {
  animation: shine 0.8s ease forwards;
  color: rgb(255, 255, 255);

}

button.stillSubmit:active {
  transform: translateY(0);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
  color: rgb(0, 0, 0);
  transition: none; /* 추가된 부분 */
}


@keyframes shine {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1);
  }
  100% {
    transform: scale(1);
    color: white;
    background-color: black;
    box-shadow: 0 4px 8px 0 rgb(172, 172, 172);
  }
}

/* 사과 메세지 */
.sorry {
  color: #a89696;
}
</style>
