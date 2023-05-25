<template>
<v-app>
    <v-container id="container">

        <v-row class="card">
            <v-col cols='12'>
                <img :src="'http://127.0.0.1:8000' + still_detail?.still.still_image" :alt="still_detail?.still.still_image" />
                <button id="exit" @click="back">X</button>
            </v-col>
            <v-row>
            <v-col cols='6' id='movie-detail'>
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
                <v-col id="footer" cols='12' align="right">
                    <v-dialog v-model="dialog" persistent width="1100">
                        <template v-slot:activator="{ props }">
                            <v-btn id="stillButton" small v-bind="props" @click="getUserCollections()" class="Collection">Still to my collection</v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">Choose Collection</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12" sm="6">
                                            <v-select v-model="pickedCollection" :items="collectionsList" label="Collection" item-value="id" return-object required></v-select>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                                    Close
                                </v-btn>
                                <v-btn color="blue-darken-1" variant="text" @click="AddToCollection">
                                    Save
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <!-- 게시글 삭제 -->
                    <v-btn id="deleteButton" small @click="deleteStill">DELETE</v-btn>
                </v-col>
            </v-col>
            <v-col cols='6' id="comments" v-if="still_detail">
                <v-col col='12'>
                    <ParentComment :still_id="still_detail.still.id" :key="componentKey" @child-comment-submit="componentKeyChange"></ParentComment>
                </v-col>
            </v-col>
            </v-row>
        </v-row>

        <v-row class="card">
            <v-col id="recommendTitle">How about these stills?</v-col>
            <v-col id="columns" style='margin: auto;'>
                <figure v-for="(still, index) in recommendStill" :key="index">
                    <StillCard :still="still" :index="index"></StillCard>
                </figure>
            </v-col>
        </v-row>
    </v-container>
</v-app>
</template>

<script>
import StillCard from "@/components/StillCard.vue";
import ParentComment from "./ParentComment.vue";
import axios from "axios";

export default {
    name: "MovieDetail",
    components: {
        StillCard,
        ParentComment,
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
            pickedCollection: null,
            myData: null,
        };
    },
    computed: {
        genre() {
            let newGenres = [];
            if (this.still_detail) {
                let newStr = "";
                for (const element of this.still_detail.movie[0].genre) {
                    if (element === "[" || element === " " || element === "'") {
                        continue;
                    } else {
                        if (element === "," || element === "]") {
                            newGenres.push(newStr);
                            newStr = "";
                        } else {
                            newStr += element;
                        }
                    }
                }
            }
            return newGenres;
        },
    },
    created() {
        this.get_detail();
        // this.getUserCollections()
    },
    methods: {
        get_detail() {
            const stillId = this.$route.params.stillId;

            axios
                .get(`http://127.0.0.1:8000/stills/detail/${stillId}/`)
                .then((response) => {
                    this.still_detail = response.data;
                    this.selectRecommend();
                })
                .catch((err) => {
                    console.error("새로고침 에러!", err);
                });
        },
        componentKeyChange() {
            this.componentKey += 1;
        },
        back() {
            this.$router.go(-1);
        },
        selectRecommend() {
            axios
                .get(
                    `http://127.0.0.1:8000/stills/recommend/${this.still_detail.still.still_color}/`
                ) // django에서 db에 저장된 해당 색상 stillcut 정보를 받아옴
                .then((response) => {
                    this.recommendStill = response.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        deleteStill() {
            const stillId = this.$route.params.stillId;
            let token = localStorage.getItem("access_token");
            axios({
                    method: "delete",
                    url: `http://127.0.0.1:8000/stills/detail/${stillId}/`,
                    headers: {
                        Authorization: "Token " + token,
                    },
                })
                .then(() => {
                    alert("삭제되었습니다.");
                    this.$router.push({
                        name: "home"
                    });
                })
                .catch(() => {
                    alert("본인이 작성한 스틸컷만 삭제할 수 있습니다.");
                });
        },
        // ◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶◀▶

        AddToCollection() {
            console.log(typeof this.pickedCollection);
            // [1] 선택된 콜렉션 값을 가져오고 - 를 기준으로 스플릿해서 인덱스 값을 뽑는다.
            let words = this.pickedCollection.split("-");
            let pk = Number(words[0].trim());
            // myData의 인덱스 pk인 오브젝트에 사용자가 선택한 콜렉션에 대한 id 정보가 저장되어있다.
            let target = this.myData[pk - 1];

            const stillId = Number(this.$route.params.stillId);
            let token = localStorage.getItem("access_token");
            console.log(typeof stillId, typeof target.id);
            axios
                .post(
                    `http://127.0.0.1:8000/stills/append/${stillId}/${target.id}/`, {
                        collection_pk: target.id,
                        still_pk: stillId,
                    }, {
                        headers: {
                            Authorization: "Token " + token,
                        },
                    }
                )
                .then(() => {
                    alert("콜렉션에 추가되었습니다.");
                })
                .catch(() => {
                    alert("콜렉션에 저장을 실패했습니다.");
                });
        },
        getUserCollections() {
            this.dialog = true;
            const username = this.$store.state.userInfo?.username;
            let token = localStorage.getItem("access_token");
            if (username) {
                axios
                    .get(`http://127.0.0.1:8000/stills/user/${username}/collections`, {
                        headers: {
                            Authorization: "Token " + token,
                        },
                    })
                    .then((response) => {
                        // JavaScript에서 forEach 함수를 사용해 배열 순회하기
                        this.myData = response.data;
                        // objects 리스트에서 특정 KEY로의 value값들을 추출하기. ARRAY.prototype.map() ,
                        // map에 람다식을 이용하여 아주 간단하게 추출한 방법이다.
                        // 지금 index 값을 꼭 반환 받아야 하는 이유는 콜렉션 네임이 같으면 v-select에서 중복 처리 되면서 없어지기 때문이다.(중요)
                        this.collectionsList = this.myData.map(
                            (row, index) => `${index + 1} - ${row.collection_name}`
                        );
                        console.log(this.collectionsList);
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            }
        },
    },
};
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
/* =======
  position: absolute;
  font-size: 20px;
  top: 1%;
  right: 1%;
  background-color: white;
  opacity: 0.8;
  padding: 1px 8px;
  border-radius: 10px;
}
*/
div#comments.col.col-6 {
  padding: 0;
}

#container {
    /* max-width: 1280px;
  min-height: 720px; */
}
div.row {
  margin: 0;
}
div.row.card {
    /* width: 90%;
  height: 90%;
  position: relative; */
    margin: 0 auto 20px auto;
    border-radius: 10px;
    background-color: white;
    box-shadow: 0 4px 8px 0 rgb(172, 172, 172);
}

div.col.col-12 {
  padding: 0;
}

img {
  width: 100%;
  border-radius: 10px 10px 0 0;
}
    /*
#cardDetail {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
/* #movie {
  width: 50%;
}
#comments {
  width: 50%;

} */

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
  
}

#stillDetailFooter {
  text-align: right;
  margin: 0 10px;
}

#columns {
  column-width: 350px;
  column-gap: 15px;
  margin: 0 10px;
}
#columns figure {
  display: inline-block;
  border:1px solid rgba(0,0,0,0.2);
  margin: 0;
  margin-bottom: 15px;
  border-radius: 20px;
}
#columns figure img {
  border-radius: 20px;
  width: 100%;
} 
#footer {
  margin: 15px 0;
  display: flex;
  flex-flow: row wrap;
  justify-content: flex-end;
}
#stillButton {
  margin: 3px 15px;
}
#deleteButton {
  margin: 3px 15px;
}
</style>
