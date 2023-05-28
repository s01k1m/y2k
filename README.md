# [STILLER] 영화 스틸컷 공유 서비스

<aside>
📌 Contents

</aside>

# 1. 개발 목적

## a. 목표

실제로 유저가 사용할만하고, 유저가 만들어가는 서비스를 개발해보자!

## b. 목적

첫 프로젝트이고, 기한이 길지 않았기 때문에 복잡하고 어려운 알고리즘을 구현하기보다는 우리가 일상에서 사용하는 웹페이지를 만들며, 개발에 이해도를 높이는 것이 이번 프로젝트의 목적이었다.

---

# 2. STILLER

## a. Why ‘STILLER’?

> **STILL**(STEAL) **THE SHOW!**
> 

**‘사람들의 주목을 끄는 서비스’** 

사람들은 영화를 다양한 방식으로 즐긴다. 그 서사를 사랑하는 사람이 있는가 하면, 영화의 장면 그 자체를 사랑하는 사람들이 있다.

우리는 영화의 장면, 색감에 주목하는 사람들을 목표로 서비스를 기획했다.

유저들은 **‘STILLER’**에서 자신이 좋아하는 영화의 스틸컷들을 공유하고 그 안에서 소통한다. 또한 좋아하는 색감을 선택하면, 해당 색감을 가진 자신이 몰랐던 영화의 장면들도 즐길 수 있다.

‘STILLER’의 지향점은 자신이 알고 있던 영화의 장면들을 공유하는 것을 넘어서, 유저에게는 자신의 취향에 맞는 영화에 대해 알게 됨으로써 다양한 영화를 즐길 수 있는 방법을, 영화 제작 측에게는 색감을 활용하는 새로운 방식의 홍보 창구를 제공하는 것이다.

## b. 주요 기능

### 1) 영화 스틸컷 공유

1. 게시글 작성
    
![create](/uploads/eb8d267097282f9ac548432ad0ba556b/create.gif)

2. 게시글 상세 정보 확인
    
![디테일페이지](/uploads/b6b5b4298a2652b9c9364d4dff7c8e9f/디테일페이지.gif)


### 2) 콜렉션 생성 및 공유

1. 콜렉션 생성
    
![콜렉션생성](/uploads/2155be17d69ece64b8e1145e22792f86/콜렉션생성.gif)
    
2. 콜렉션 확인
3. 콜렉션 삭제
    
![콜렉션스틸추가콜렉션삭제](/uploads/e8887a0cd3cd7e7cb69641740f3bb12b/콜렉션스틸추가콜렉션삭제.gif)

### 3) 커뮤니티

1. 댓글, 대댓글 작성
2. 댓글, 대댓글 삭제
    
![댓글](/uploads/b4ffe1ca23093068440f35d5fe1963c0/댓글.gif)  

---

# 3. 구현

## a. Y2K

### 1) R&R

SOLK(팀장), KIMU(팀원)

| 기능 | FE/BE | URL | request body | response | 담당 |
| --- | --- | --- | --- | --- | --- |
| 인트로 페이지 | FE | / |  |  | SOLK, KIMU |
| 메인 페이지 | FE | /home |  |  | KIMU |
| 회원가입 페이지 | FE | /signup |  |  | SOLK |
| 로그인 페이지 | FE | /login |  |  | SOLK |
| Still 작성페이지 | FE | /create |  |  | SOLK |
| 검색 페이지 | FE | /search/:params |  |  | SOLK |
| 마이 페이지 | FE | /user |  |  | SOLK |
| 콜렉션 페이지 | FE | /stills |  |  | KIMU |
| Still 상세 정보 가져오기 | BE | /home/detail/${스틸 id} |  | 성공시(200) | KIMU |
| 로그인 | BE | /accounts/login/ | {
username,
email,
password1,
password2
} |  | KIMU |
| 회원 가입하기 | BE | /accounts/signup/ | {
username,
password
} |  | KIMU |
| 사진 등록 위해 영화 검색하기 | BE | /create/getmovie/${encodedQuery} | {
serachQuery: encodedQuery
} | {
"id": 319,
"movie_id": 299534,
"movie_title": "어벤져스: 엔드게임",
"overview": "어벤져스의 패배 이후...",
"movie_released_date": "2019-04-24",
"genre": "['모험', 'SF', '액션']"
},
{
"id": 419,
"movie_id": 99861,
"movie_title": "어벤져스: 에이지 오브 울트론",
"overview": "토니 스타크는 뉴욕전쟁 때….",
"movie_released_date": "2015-04-22",
"genre": "['액션', '모험', 'SF']"
},
{
"id": 1023,
"movie_id": 1771,
"movie_title": "퍼스트 어벤져",
"overview": "진주만 공습을 겪은 미국은...",
"movie_released_date": "2011-07-22",
"genre": "['액션', '모험', 'SF']"
}
] | SOLK |
| 사진 등록하기 | BE | /create/${스틸 id} | {
still_iamge,
movie_id
} | 성공시(200)
실패시(401) | SOLK |
| 댓글, 대댓글 등록하기 | BE | communities/${still_id}/ | {
'content': this.comment_content,
'parent': null,
} | 성공시(201)
실패시(401) | KIMU |
| 댓글, 대댓글 삭제하기 | BE | communities/${id}/delete/ |  | 성공시(201)
실패시(401) | KIMU |
| 댓글, 대댓글 가져오기 | BE | /communities/${still_id} |  | [
{
"id": 4,
"username": "sol",
"content": "이 장면 정말 좋아요",
"still": 2,
"user": 2,
"parent": null
},
{
"id": 5,
"username": "yujin",
"content": "맞아요. 멋있어요.",
"still": 2,
"user": 3,
"parent": 4
},
{
"id": 6,
"username": "luka",
"content": "어벤져스 1 최고에요",
"still": 2,
"user": 4,
"parent": 4
}
] | KIMU |
| 사진을 개인 콜레션에 추가하기 | BE | /home/detail/${스틸 id}/collect/${콜렉션 id} |  | 성공시(200)
실패시(401) | SOLK |
| 영화로 사진 검색하기 | BE | stills/search/${this.$route.params.searchInput}/ |  | [
{
"id": 2,
"still_image": "/media/stills/avenger2.gif",
"still_color": "PURPLE",
"movie_id": 270,
"user": 2
},
{
"id": 4,
"still_image": "/media/stills/avengers13.gif",
"still_color": "GREY",
"movie_id": 270,
"user": 2
},
{
"id": 5,
"still_image": "/media/stills/avengers1.gif",
"still_color": "YELLOW",
"movie_id": 270,
"user": 2
},
{
"id": 3,
"still_image": "/media/stills/avenger-endgame.gif",
"still_color": "BLACK",
"movie_id": 319,
"user": 2
},
{
"id": 7,
"still_image": "/media/stills/avengers2.gif",
"still_color": "BLUE",
"movie_id": 419,
"user": 2
}
] | SOLK |
| 개인 유저 사진 다 가져오기 | BE | /stills/user/${username}/stills/ |  | [
{
"id": 2,
"still_image": "/media/stills/avenger2.gif",
"still_color": "PURPLE",
"movie_id": 270,
"user": 2
},
{
"id": 3,
"still_image": "/media/stills/avenger-endgame.gif",
"still_color": "BLACK",
"movie_id": 319,
"user": 2
},
{
"id": 4,
"still_image": "/media/stills/avengers13.gif",
"still_color": "GREY",
"movie_id": 270,
"user": 2
},
……….
{
"id": 15,
"still_image": "/media/stills/harrypotter-knight2.jpg",
"still_color": "RED",
"movie_id": 471,
"user": 2
},
{
"id": 16,
"still_image": "/media/stills/harrypotter2.jpg",
"still_color": "ORANGE",
"movie_id": 216,
"user": 2
},
{
"id": 17,
"still_image": "/media/stills/harrypotter.jpg",
"still_color": "RED",
"movie_id": 216,
"user": 2
}
] | SOLK |
| 개인 유저 콜렉션 다 가져오기 | BE | /stills/user/${username}/collections/ |  | [
{
"id": 20,
"user": 2,
"username": "sol",
"collection_name": "콜렉션1",
"stills": [
{
"id": 10,
"still_image": "/media/stills/coraline4.gif",
"still_color": "GREEN",
"movie_id": 314,
"user": 2
},
{
"id": 22,
"still_image": "/media/stills/jojo-rabbit4.jpg",
"still_color": "WHITE",
"movie_id": 1975,
"user": 2
}
]
},
{
"id": 21,
"user": 2,
"username": "sol",
"collection_name": "콜렉션2",
"stills": []
}
] | SOLK |
| 개인 유저 콜렉션 생성하기 | BE | stills/user/${username}/collections/ | {
collection_name : collection_title
} | 성공시(200)
실패시(401) | SOLK |
|  개인 유저 콜렉션 삭제하기 | BE | stills/user/${username}/collection/delete/${collection_id}/ |  | 성공시(200)
{
"message": "콜렉션이 삭제되었습니다."
} | SOLK |
| 모든 유저 콜렉션 다 가져오기 | BE | /stills/collections/all/ |  | [
{
"id": 1,
"user": 2,
"username": "sol",
"collection_name": "콜렉션1",
"stills": [
{
"id": 46,
"still_image": "/media/stills/%EC%97%94%EC%B9%B8%ED%86%A02.gif",
"still_color": "ORANGE",
"movie_id": 145,
"user": 2
}
]
},
{
"id": 2,
"user": 2,
"username": "sol",
"collection_name": "콜렉션1",
"stills": []
},
{
"id": 3,
"user": 2,
"username": "sol",
"collection_name": "콜렉션2",
"stills": []
},
{
"id": 4,
"user": 3,
"username": "yujin",
"collection_name": "yj 콜렉션",
"stills": [
{
"id": 49,
"still_image": "/media/stills/%EC%8A%AC%EB%9E%A8%EB%8D%A9%ED%81%AC1.gif",
"still_color": "BLACK",
"movie_id": 737,
"user": 3
}
]
}
] | KIMU |

## b. 기획

### 1) ERD

![싸피_팀프로젝트.drawio__1_.svg](/uploads/a4dbd8e6b360475d06e3fe77935c8fa9/싸피_팀프로젝트.drawio__1_.svg)


### 2) Component

![STILLER_Coponents (3).drawio.svg](src/STILLER_Coponents_(3).drawio.svg)

## c. 기능

### 1) 색상 별 추천 알고리즘

<aside>
✔️ 스틸컷을 create하면, 색상 분류 로직을 통과해 특정 색상으로 분류되어 화면에 보여진다.

</aside>

1. `colorThief` 라이브러리를 활용해 이미지에서 가장 많은 비율을 차지하고 있는 색상의 r, g, b값을 뽑아낸다.
2. 해당 r, g, b 값을 크게 10가지 색상으로(빨, 주, 노, 초, 파, 분, 보, 흰, 회, 검) 분류한다
    1. 예를 들면 흰색은 3가지 색상 값이 200 이상이며, r 값이 가장 크고 나머지 두 값이 일정 값 이하이면 빨강이다.
3. 스틸컷을 등록할 때 Django views에서 해당 로직을 통과해 대표 색상을 db에 저장한다.
4. front에서 특정한 색상으로 접근하면, 해당 색상을 가진 obj들을 필터링해서 가져와 화면에 뿌려준다.
    1. 기본 선택 색상은 ‘ALL’로, 모든 스틸컷들을 보여준다. (새로고침 시에도)

### 2) 영화 검색 알고리즘

<aside>
✔️ nav bar의 search bar에 영화를 검색하면 그 영화의 스틸컷으로 저장된 모든 stills가 검색된다.

</aside>

1. DB에 영화 정보가 저장되어있다.
2. 서치바의 input value를 사용자가 입력하면 searchQuery에 바인딩한다.
    
    → searchQuery = “art”
    
3. 입력된 searchQuery를 params에 담아 axios로 장고로 넘겨준다.
4. 장고 내에서 searchQeury와 movie_title가 부분 일치하는 모든 Movie objects를 검색한다.
5. Movie Objects 리스트의 id 값들을 모두 뽑아 저장된 모든 stills에서 id 리스트 값들이 일치하는 것들을 검색하여 vue로 반환한다.
    
    → return 영화 제목에 “art”가 대소문자를 상관하지 않고 포함된 모든 스틸들
    

### 3) 콜렉션 생성과 콜렉션에 still 객체 추가

<aside>
✔️ 마이 페이지에서 유저는 개인 콜렉션을 생성할 수 있다. 유저는 그 콜렉션에 마음에 드는 still 객체를 저장할 수 있다.

</aside>

콜렉션 생성

1. 콜렉션의 이름을 input 으로 받는다.
2. 콜렉션 테이블에 still은 아무것도 저장되지 않은 텅 빈 콜렉션 row를 생성한다.

still 객체 추가

한 개의 still를 어떠한 콜렉션에 추가하기 위해서 유저는 어떤 still과 어떤 콜렉션인지 지정해야한다. 그래서 still detail 페이지에서 collection을 한개 선택하여 추가할 수 있는 버튼을 만들기로 하였다. 버튼이 작동하기 위해서는 콜렉션이 무엇이 있는지 받아와야 한다. 

1. 이 유저의 id값을 통해 이 유저가 만든 콜렉션를 다 받아온다.
2. 콜렉션의 objects 리스트를 반환받으면 이것을 가공해야한다. 왜냐하면 vuetify에는 `v-select :items`에 이름 리스트를 바인딩해줘야하기 때문이다.
    
    따라서 콜렉션 이름을 뽑아 새로운 리스트**를 형성한다. 이 리스트를 v-input type=’select’ 에 연결한다.
    
    **(주의할 점) 같은 이름의 콜렉션이 여러개 있으면 리스트로 v-input과 연결되면서 중복이 제거되는 현상이 생긴다. 따라서 `index+1:collection_title` 과 같이 중복처리 되지 않게 가공해야한다.
    
    ```jsx
    <v-select
      label="Select"
      :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
    ></v-select>
    ```
    
3. still_id, collection_id를 axios로 넘겨 장고 DB에 저장한다. 장고에서 ManytoMany로 연결되어 중계테이블이 자동생성되었다.

### 4) 댓글, 대댓글

<aside>
✔️ 스틸컷 상세 페이지에서 댓글을 작성 및 삭제하면, SPA 방식으로 즉각적으로 화면의 일부가 변화한다.

</aside>

1. 특정 스틸컷 상세 페이지에서 댓글을 작성하면, front에서 Django으로 해당 스틸컷 id 값을 전달해준다.
    1. 만일 해당 댓글이 대댓글이라면, 부모 댓글의 pk 값도 같이 전달해준다.
2. 부모 pk 값이 있으면 해당 값을 `parent` 필드에 넣어주고, 없다면 생략한다.
    1. 모델에 `parent` 필드는 반드시 `null=True`로 해주어야 한다.
3. 유효성 검사 후 db에 저장한다.
4. front에서 특정 스틸컷 상세 페이지에서 해당 스틸컷 id 값으로 필터링한 데이터를 받아온다.
    1. 이 중에서, `parent` 값이 있는 댓글들은 대댓글로 분류한다.
5. front 댓글 컴포넌트 처리 과정은 MovieDetail → ParentComment → ChildComment
    1. SPA 적용을 위해서, MovieDetail에 동적 데이터를 props해주며, 자식, 부모 댓글에 변화가 생길 때마다 emit 이벤트를 발생시켜 최종적으로는 MovieDetail에 돌아와 해당 동적 데이터 값에 변화를 준다.
6. 댓글 삭제 시에는 댓글 id 값을 Django에 전달해 db에서 해당 데이터를 삭제한다.

## d. 에러 정리

### 1) CREATE unvalid image error

> **🚨 에러 메세지**
> 
> 
> ```bash
> 
> serializer:  PostSerializer(data={'still_image': <InMemoryUploadedFile: black rose.jpeg (image/jpeg)>, 'user': 2, 'still_color': 'BLACK', 'movie_id': '7'}):
>     id = IntegerField(read_only=True)
>     still_image = ImageField(allow_null=True, max_length=100, required=False)
>     still_color = CharField(allow_blank=True, max_length=6, required=False)
>     movie_id = PrimaryKeyRelatedField(queryset=Movie.objects.all())
>     user = PrimaryKeyRelatedField(queryset=User.objects.all())
> ♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎
> {'still_image': [ErrorDetail(string='Upload a valid image. The file you uploaded was either not an image or a corrupted image.', code='invalid_image')]}
> ```
> 

`✔️ **가능한 해결방법**` 

1. File format: Make sure the file is in a supported image format, such as JPEG, PNG, GIF, etc. Double-check the file extension (.jpeg, .jpg, .png, etc.) to ensure it matches the actual file format.
2. File content: Verify that the file you're trying to upload is not corrupted or damaged. Try opening the image file on your computer using an image viewer to confirm its integrity.
3. Reinstall Pillow

**`☑️ 해본 시도`**

1, 2 ⇒ 문제 없음 확인 완료. django admin 페이지에서 등록하면 db에 잘 저장되는 이미지였음

3 ⇒ pillow 패키지도 문제 없음 확인 완료

4 ⇒ `serializers.py` 에서 이미지 유효성 검사를 실시 → 여전히 에러

```python
from PIL import Image
from django.core.exceptions import ValidationError

def validate_image(image):
    try:
        img = Image.open(image)
        img.verify()
    except Exception:
        raise ValidationError('Invalid image file')

class YourSerializer(serializers.ModelSerializer):
    still_image = serializers.ImageField(validators=[validate_image])
    
    class Meta:
        model = STILL
        fields = '__all__'
```

5 ⇒ 구글 서치를 해도 자료가 적었고 이것을 해결하기 보다 인풋과 필드를 살짝 고치면 될 것 같다는 생각이 들었음 → 해결

**`✅ 해결 방법`**

```bash
(Django) ImageField ⇒ FileField 로 변경

(Vue) Input only png, jpg, jpeg, gif로 변경
```

### 2) 이미지가 장고 /media/에서 가져오지 못하는 현상

**`✅ 해결 방법`**

1. 주소 작성 방식 수정 → 해결
    - 예시:  `<img :src="'127.0.0.1:8000/media/'+f.fundraiser.fundraiserImage.url">`
    - [https://stackoverflow.com/questions/62050553/django-vue-js-cant-display-images-from-database](https://stackoverflow.com/questions/62050553/django-vue-js-cant-display-images-from-database)
    - [https://stackoverflow.com/questions/75224726/vue-js-are-not-displaying-images-from-django-media-folder](https://stackoverflow.com/questions/75224726/vue-js-are-not-displaying-images-from-django-media-folder)
2. `<img :src="require(@/assets/${변수명}.png)">`

### 3) 초기 Intro 진입 시 로그인을 체크하는 안내 창이 뜨는 현상

**`✅ 해결 방법`**

1. 로그인 체크를 안하고 싶은 URL을 지정해 로그인 체크 로직 가장 처음에 확인

```jsx
let except_url = new Array('http://localhost:8080/')

if (except_url.includes(current_url)){
  console.log("지금 페이지는", current_url, "로그인 검사를 안 합니다."
  )
```

### 4) 로그인 확인이 필요한 페이지에 비정상적인 루트로 진입할 시 확인을 안하는 현상

**`✅ 해결 방법`**

1. 페이지에 들어갈 때마다 로그인을 확인하는 것이 아닌, router에서 이동하기 전 마다 실행하는 `beforeEach` 사용
2. 로그인 여부는 로컬스토리지에서 접근 토큰을 가져와 저장 후 판별에 이용

```
const isLoggedIn = localStorage.getItem('access_token')
	...
router.beforeEach((to, from, next) => {
  console.log('from!', from)
  console.log('to!', to)
  // 로그인 여부
  // 로그인이 필요한 페이지 지정
  const authPages = ['create']
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    console.log('Login으로 이동')
    alert('로그인이 필요한 페이지입니다.')
    next({ name: 'login'})
  } else {
    console.log('to로 이동!')
    next()
  }
```

### 5) 새로고침 시 데이터가 안 뜨는 현상

**`✅ 해결 방법`**

1. 기존에는 홈에서 카드 컴포넌트로 들어가면 해당 컴포넌트에서 axios 요청을 해서 스틸컷 디테일을 받아왔었다.
2. 이후 스틸id와 스틸detail을 param으로 넘겨줬었다.
    - 이때 발생한 에러가, 새로고침 시 스틸 detail을 받아오지 않아서 화면에 보여지지 않았던 것이다.
3. 따라서 param으로는 스틸 id만 전달하고, 스틸컷 디테일 페이지에서 매번 axios 요청으로 디테일을 받아오게 수정했다.

### 6) Detail 페이지 recommend에서 스틸컷 클릭시 해당 스틸컷 디테일로 이동하지 않는 현상

**`✅ 해결 방법`**

1. key를 통해 경로 개체 속성을 강제로 연결시켜주는건데, 보여지는 화면에 쿼리 및 해시가 포함된 전체 URL을 연결하여 쿼리스트링이 변경될때마다, 즉 탐색하는 이벤트가 발생할때 마다 페이지를 다시 리로드해서 노출시키는 방법을 적용했다.

```jsx
<router-view :key="$route.fullPath"/>
```

### 7) Mypage에서 새로고침하면 User가 undefined 되면서 userStills, userCollections가 불러와지지 않는 현상

`**📌 원인**`

1. `store`에서 uesrinfo 를 db에서 확인해서 가져오는 로직이  `getUserStills`, `getUserCollections` 로직 보다 나중에 실행되기 때문이다.

**`✅ 해결 방법`**

1. 매번 userinfo를 DB에서 조회하지 않고 token 처럼 localStorage에 저장한다. 

## e. what we learned

### 1) git branch

local에서 merge 한 후 push 하면 꼭 알려주기

1. `git switch -c { branch name }` 으로 branch를 생성하면서 이동 후 작업 진행!!!!
2. branch에서 작업 완료 하면`git add .` 
3. `git commit -m { 커밋 내용 }` 남긴 후
4. `git switch main`   으로 main branch로 이동
5. `git pull` 해서 최신 main으로 update하기
6. `git merge {병합할 branch 이름}`  으로 병합
7. `git push`
8. **상대방에게 Pull 하라고 말해주기**
9. `git branch -d {지울 branch}`  으로  branch 지우기

### 2) 중계 테이블

- 중계 테이블은 중계 테이블에 관계하는 테이블 foreignkey외에 다른항목을 추가하고자 할 때 필요하다.
- 중계테이블을 안 만들고 Many to Many옵션을 지정하면 데이터베이스에 자동으로 관계테이블이 생성된다.
    - 이 테이블에 컬럼을 추가하고자 하면 직접 장고에서 만들어야 추가하고자 하는 컬럼이 반영된다.

### 3) API에서 데이터를 추출해 JSON으로 변환

```python
import requests
import json
from pprint import pprint

file_path = "./movie_data.json"

# API 지정
apikey = ""

# 정보를 알고 싶은 영화 리스트 만들기
movie_list = range(1, 100)

# API 지정
movie_api = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}&api_key={key}"
genre_api = "https://api.themoviedb.org/3/genre/movie/list?language=ko-KR&api_key={key}"

# string.format_map() 매핑용 클래스 만들기
class Default(dict):
    def __missing__(self, key):
        return key

# 장르정보 추출
# API의 URL 구성하기
url = genre_api.format_map(Default(key=apikey))
# API에 요청을 보내 데이터 추출하기
r = requests.get(url)  # json 형태의 데이터가 나온다.
# 결과를 JSON 형식으로 변환하기
raw_data = json.loads(r.text)['genres']
genre_list = {}
for genre in raw_data:
    genre_list[genre['id']] = genre['name']

data = []
cnt = 1
# 각 영화의 정보 추출하기
for page in movie_list:
    # print(f"#############{page}#############")
    # API의 URL 구성하기
    url = movie_api.format_map(Default(page=page, key=apikey))
    # API에 요청을 보내 데이터 추출하기
    r = requests.get(url)  # json 형태의 데이터가 나온다.
    # 결과를 JSON 형식으로 변환하기
    raw_data = json.loads(r.text)['results']

    for d in raw_data:
        movie = {"model" : "stills.movie", "pk": cnt, "fields" : {}}
        movie["fields"]['movie_id'] = d['id']
        movie["fields"]['movie_title'] = d['title']
        try:
            movie["fields"]['movie_released_date'] = d['release_date']
        except:
            continue
        movie["fields"]['overview'] = d['overview']
        movie["fields"]['genre'] = []
        for genre in d['genre_ids']:
            movie["fields"]['genre'].append(genre_list[genre])
        data.append(movie)
        cnt += 1

with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

print('finished')
```

### 4) **v-show VS v-if**

- **v-show (Expensive initial load, cheap toggle)**
    - 표현식 결과와 관계 없이 렌더링 되므로(숨김 처리)
    초기 렌더링에 필요한 비용은 v-if 보다 높을 수 있음
    - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
    - 처음엔 안띄우지만, 나중에 띄울 일이 있을 때 사용
- **v-if (Cheap initial load, expensive toggle)**
    - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로
    초기 렌더링 비용은 v-show 보다 낮을 수 있음
    - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음
    - 처음부터 끝까지 다시 띄울 일이 없을 때 사용

### 5) git 중간에 파일 이름 변경

- 프로젝트 중간에 파일 이름을 바꾸면 깃에 올라가지 않음
- 따라서 특정 명령어로 변경해야 함

```bash
git mv oldName newName
```

---

# 소감

<aside>
👩 SOLK :

1. 정해진 짧은 시간 내에 해낸 것에 아주 큰 놀라움을 느낀다. 해냈다는 성취감과 함께 앞으로 만날 프로젝트들이 기대가 되는 계기가 되었다.
2. CREATE 페이지에서 이미지 파일을 백에 전달하는 코드를 짜면서 많은 시행착오를 겪었다. 괴로웠지만✨ 이제는 웃을 수있다. ㅜㅜ금요일을 날리고 주말동안 하루종일 공부하면서 그때 어떠한 계단을 오른 것 같다. 공식문서와 친해졌다는 점이 최고로 기쁘다.
    
    ![Untitled](src/Untitled.png)
    
3. 유진님 고마워요! 페어와의 소통이 즐거웠고 그래서 프로젝트가 재미있었다. 유진님과 함께여서 포기하지 않고 달릴 수 있었어요! 🧡
</aside>

<aside>
👩 KIMU :

1. 본격적인 서비스 구현이 처음이었고, 백과 프론트를 모두 구현해야 했기에 요청과 응답의 흐름을 이해하는데 꽤나 시간이 걸렸었다. 하지만 역시 반복 연습의 결과로.. 드디어 하나의 서비스를 구현하기 위한 어느정도의 실력이 갖추어진 것 같다.
2. 페어와 아이디어를 상의하고, 이를 구체화하는 과정이 모두 즐거웠다. 혼자서는 생각해내지 못 할 법한 아이디어나, 구현 방법들을 페어와 함께 상의하며 절충해나갔기에, 우리의 서비스가 더 완성도가 높아지지 않았나 싶다.
3. 코드 구현을 위해 장고와 뷰의 개념을 처음부터 다시 짚어가면서, 기초 지식이 더 두터워질 수 있었다. 또한 예상치 못한 다양한 에러를 만나면서, 이를 해결하는 경험이 구현 능력 향상에 큰 도움이 되었다.
4. 쏠님과 페어를 하게 되어서 정말 신께 감사드려야 할 정도입니다. 덕분에 많이 배웠어요 정말로! 우리 정말 고생했어요! 특히 쏠님 정말 고생했어요!! 알라뷰
</aside>
