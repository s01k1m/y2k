<template>
  <div class="moviedetail">
    <v-container id="container">
      <div class="card">
        <img :src="'http://127.0.0.1:8000' + stillDetail.still.still_image" :alt="stillDetail.still.still_image">
        <button id="exit" @click="back">X</button>
        <div id="cardDetail">
          <div id="movie">
            <div id="released_date">
              {{ stillDetail.movie[0].movie_released_date }} released
              <span id="genre">
                <span v-for="(name, index) in genre" :key="index">
                  {{ name }}
                </span>
              </span>
            </div>
            <div id="title">
              {{ stillDetail.movie[0].movie_title }}
            </div>
            <div id="overview">
              {{ stillDetail.movie[0].overview }}
            </div>
          </div>
          <div id="comments">Comments
            <div v-for="(comment, index) in comment_list" :key="index">
              <ParentComment :comment="comment" :child_comment_list="parseChildC(comment.id)"></ParentComment>
            </div>
            <div>
              댓: <input type="text" @keyup.enter="commentSubmit" v-model="comment_content">
            </div>
          </div>
        </div>
      </div>
      <div class="card">
        <div id="recommendTitle">
          How about these stills?
        </div>
        <div id="columns">
          <figure v-for="(still, index) in recommendStill" :key="index">
            <StillCard :still="still" :index="index"></StillCard>
          </figure>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import StillCard from '@/components/StillCard.vue'
import ParentComment from './ParentComment.vue'
import axios from "axios"

export default {
  name: 'MovieDetail',
  components: {
    StillCard,
    ParentComment
  },
  data() {
    return {
      recommendStill: [],
      comment_list: [],
      child_comment_list: [],
      comment_content: null, 
    }
  }, 
  computed: {
    stillDetail() {
      return this.$route.params.stillDetail
    },
    genre() {
      let newGenres = []
      let newStr = ''
      for (const element of this.stillDetail.movie[0].genre) {
        if (element === '[' || element === ' ' || element === '\'') {
          continue
        } else {
          if (element === ',' || element === ']') {
            newGenres.push(newStr)
            newStr = ''
          } else {
            newStr += element
          }
        }
      }
      return newGenres
    },
  },
  created() {
    this.selectRecommend()
    this.get_comment_list()
  },
  methods: {
    parseChildC(parent){
      return this.child_comment_list.filter((comment)=>{
        return comment.parent === parent
      })
    },
    back() {
      this.$router.push({ name: 'home' })
    },
    selectRecommend() {
      axios
      .get(`http://127.0.0.1:8000/stills/recommend/${this.stillDetail.still.still_color}/`) // django에서 db에 저장된 해당 색상 stillcut 정보를 받아옴
      .then((response) => {
        this.recommendStill = response.data
      })
      .catch((error) => {
        console.error(error);
      });
    },
    get_comment_list() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/communities/${this.stillDetail.still.id}`
      })
      .then((response) => {
        response.data.forEach(element => {
          if (!element.parent){
            this.comment_list.push(element)
          } else {
            this.child_comment_list.push(element)
          }
        });
      
      })
      .catch((err) => {
        console.log('err: ', err)
      })
    },
    commentSubmit(e) {
      e.preventDefault()
      if (!this.comment_content) {
        alert('내용을 입력하세요.')
      } else {
        console.log('commentSubmit 진입!')
        let token = localStorage.getItem("access_token")
        console.log('token: ', token)
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/communities/${this.stillDetail.still.id}/`,
          data: {
            'content': this.comment_content,
            'parent': null,
          },
          headers: {
              Authorization: "Token " + token,
          },
        })
        .then((response) => {
          console.log('댓글 작성 성공', response)
          this.comment_content = ''
          this.get_comment_list()
        })
        .catch((err) => {
          console.log('err: ', err)
        })
      }
    }
  }
}

</script>

<style scoped>
#exit {
  position: absolute;
  font-size: 20px;
  top: 1%;
  right: 1%;
  background-color: white;
  opacity: 0.8;
  padding: 1px 8px;
  border-radius: 10px;
}
#container {
  max-width: 1280px;
  min-height: 720px;
}
.card {
  width: 90%;
  height: 90%;
  position: relative;
  margin: 5px auto 20px auto;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 4px 8px 0 rgb(172, 172, 172);
}

img {
  width: 100%;
  border-radius: 10px 10px 0 0;
}
#cardDetail {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
#movie {
  width: 50%;
}
#comments {
  width: 50%;
}
#title {
  text-align: left;
  font-size: 28px;
  font-weight: 600;
  margin: 10px 15px;
}
#released_date {
  font-size: 16px;
  margin: 15px;
  text-align: left;
}

#genre {
  font-size: 16px;
  font-style: italic;
  margin: 15px;
  text-align: left;
}

#overview {
  font-size: 16px;
  margin: 15px 15px;
  text-align: left;
}

#recommendTitle {
  text-align: center;
  font-size: 28px;
  font-weight: 600;
  margin: 10px 15px;
}

#columns{
    column-width:350px;
    column-gap: 15px;
    margin: 0 10px;
}
#columns figure{
  display: inline-block;
  /* border:1px solid rgba(0,0,0,0.2); */
  margin:0;
  margin-bottom: 15px;
  border-radius: 20px;
  /* box-shadow: 2px 2px 5px rgba(0,0,0,0.5);; */
}
#columns figure img{
  border-radius: 20px;
  width:100%;
}

</style>