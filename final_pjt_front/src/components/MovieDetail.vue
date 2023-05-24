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
          <div id="comments" v-if="still_detail">
            <ParentComment :still_id="still_detail.still.id" :key="componentKey" @child-comment-submit="componentKeyChange"></ParentComment>
            <br>  
          </div>
        </div>
        <div id="stillDetailFooter">
          <!-- <button @click="AddToCollection">Add To STILLs</button> -->
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



    <!-- %%%%%%%%%%%%%%%% 아래는 콜렉션 선택을 위한 모달 팝업창 코드 %%%%%%%%%%%%%%%%%%%% -->
    <v-app>
      <v-container>
        <!-- mypage nav button -->
        <v-row>

            <!--  -->
            <v-dialog v-model="dialog" persistent width="1100">
              <template v-slot:activator="{ props }">
                <v-btn
                  small
                  v-bind="props"
                  @click="dialog = true"
                  class="create_Collection"
                  >Still to my collection</v-btn
                >
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">Choose Collection</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-select
                        v-model="pickedCollection"
                        :items="collectionsList"
                        label="Collection"
                        item-value="id"
                          return-object
                        required
                        @change="currentDataItems"
                      ></v-select>
                    </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="dialog = false"
                  >
                    Close
                  </v-btn>
                  <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="AddToCollection"
                  >
                    Save
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <!-- 콜렉션을 추가하는 버튼 -->

        </v-row>
      </v-container>
    </v-app>
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
      dialog: false,
      // 콜렉션 디비 오브젝트 데이터 (즉 원본)
      collectionsResult: null,
      // 이름 값만 배열로 가공한 데이터
      collectionsList: null,
      // 선택된 컬렉션 값
      chapterIdFilter: null,
      // 
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
    this.getUserCollections()

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
    // ◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶
    currentDataItems () {
      console.log('1',this.chapterIdFilter)

      console.log('2', this.chapterIdFilter)
      
    },
    AddToCollection() {
      //POST: http://127.0.0.1:8000/stills/append/1/1/ 
      // const stillID = this.$route.params.stillId
      // let token = localStorage.getItem('access_token')

      // data = {
      //   'collection_pk' : 1,
      //   'still_pk': stillID,

      // }

      // axios(

        
        // ))
        let str = this.chapterIdFilter
        let words = str.split('-');
        let pk =  document.write(words[0].trim());
        console.log(this.pickedCollection, pk)
      
    },
    getUserCollections() {
      const username = this.$store.state.userInfo?.username;
      let token = localStorage.getItem('access_token')
      if (username) {
        axios
          .get(`http://127.0.0.1:8000/stills/user/${username}/collections`, {
            headers: {
              Authorization: "Token " + token,
            }})
          .then((response) => {
            
            // JavaScript에서 forEach 함수를 사용해 배열 순회하기
            let myData = response.data
            // objects 리스트에서 특정 KEY로의 value값들을 추출하기. ARRAY.prototype.map() , 
            // map에 람다식을 이용하여 아주 간단하게 추출한 방법이다.
            // 지금 index 값을 꼭 반환 받아야 하는 이유는 콜렉션 네임이 같으면 v-select에서 중복 처리 되면서 없어지기 때문이다.(중요)
            myData = myData.map((row, index) => `${index} - ${row.collection_name}`)
            this.collectionsList = myData
            console.log(this.collectionsList)
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
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