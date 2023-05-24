<template>
  <div class="moviedetail">
    <v-container id="container">
      <div class="card">
        <img :src="'http://127.0.0.1:8000' + still_detail?.still.still_image" :alt="still_detail?.still.still_image">
        <button id="exit" @click="back">X</button>
        <div id="cardDetail">
          <div id="movie">
            <div id="released_date">
              {{ still_detail?.movie[0].movie_released_date }} released
              <span id="genre">
                <span v-for="(name, index) in genre" :key="index">
                  {{ name }}
                </span>
              </span>
            </div>
            <div id="titlebox">
              <span id="title">
                {{ still_detail?.movie[0].movie_title }}
              </span>
              <span id="still_color">
                # {{ still_detail?.still.still_color }}
              </span>
            </div>
            <div id="overview">
              {{ still_detail?.movie[0].overview }}
            </div>
          </div>
          <div id="comments" v-if="still_detail">Comments<br>
            <ParentComment :still_id="still_detail.still.id" :key="componentKey" @child-comment-submit="componentKeyChange"></ParentComment>
            <br>  
          </div>
        </div>
        <div id="stillDetailFooter">
          <button @click="AddToCollection">Add To STILLs</button>
          <button @click="deleteStill">DELETE</button>
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
      componentKey: 0,
      still_detail: null,
    }
  }, 
  computed: {
    genre() {
      let newGenres = []
      if (this.still_detail){      
        let newStr = ''
        for (const element of this.still_detail.movie[0].genre) {
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
      }
      return newGenres
    },
  },
  created() {
    this.get_detail()
  },
  methods: {
    get_detail() {
      const stillId = this.$route.params.stillId
      
      axios
      .get(`http://127.0.0.1:8000/stills/detail/${stillId}/`)
      .then((response) => {
        this.still_detail = response.data
        this.selectRecommend()
      })
      .catch((err) => {
        console.error('새로고침 에러!', err)
      })
    },
    componentKeyChange() {
      this.componentKey += 1
    },
    back() {
      this.$router.go(-1)
    },
    selectRecommend() {
      axios
      .get(`http://127.0.0.1:8000/stills/recommend/${this.still_detail.still.still_color}/`) // django에서 db에 저장된 해당 색상 stillcut 정보를 받아옴
      .then((response) => {
        this.recommendStill = response.data
      })
      .catch((error) => {
        console.error(error);
      });
    },
    deleteStill() {
      const stillId = this.$route.params.stillId
      let token = localStorage.getItem("access_token")
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/stills/detail/${stillId}/`,
        headers: {
          Authorization: 'Token ' + token,
        },
      })
      .then(() => {
        alert('삭제되었습니다.')
        this.$router.push({ name: 'home'})
      })
      .catch(() => {
        alert('본인이 작성한 스틸컷만 삭제할 수 있습니다.')
      })
    },
    AddToCollection() {
      
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

#titlebox {
  text-align: left;
}

#title {
  font-size: 28px;
  font-weight: 600;
  margin: 10px 15px;
}

#still_color {
  font-style: italic;
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

#stillDetailFooter {
  text-align: right;
  margin: 0 10px;
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