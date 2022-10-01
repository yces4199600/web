<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand ">FCU Shop</a>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>


      <div class="collapse navbar-collapse" id="navbarSupportedContent" v-if= checkstate()>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link active" aria-current="page" :class="isAdmin">首頁</router-link>
          </li>
        </ul>
        <ul class="navbar-nav mb-2 mb-lg-0 d-flex not-login" >
          <li class="nav-item" >
            <router-link to="/login" class="nav-link" >登入</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/signup" class="nav-link">註冊</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/cart" class="nav-link">購物車({{num}})</router-link>
          </li>
        </ul>
      </div>
      <div class="collapse navbar-collapse" id="navbarSupportedContent" v-else>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link active" aria-current="page" :class="isAdmin">首頁</router-link>
          </li>
        </ul>
        <ul class="navbar-nav mb-2 mb-lg-0 d-flex not-login" >
          <li class="nav-item">
            <router-link to="/cart" class="nav-link">購物車({{num}})</router-link>
          </li>
          <li class="nav-item">
            <a @click="logout()" class="nav-link" href="">登出</a>
          </li>
        </ul>
      </div>


      <button class="btn btn-outline-success my-2 my-sm-0" type="submit" data-toggle="modal" data-target="#searchBotton">Search</button>
      <button class="btn btn-outline-warning my-2 my-sm-0" type="submit" data-toggle="modal" data-target="#createBotton"  v-if="adminshow">Create</button>
    </div>
  </nav>

<!-- Modal -->
<div class="modal fade windowset1" id="searchBotton" tabindex="-1" role="dialog">
  <div class="modal-dialog windowset" role="document">
    <div class="modal-content windowset2">
      <div class="modal-header">
        <h5 class="modal-title">FCU SHOP</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <input type="text" class="form-control" placeholder="商品名稱" id="productKeyword" v-model="key" >
      </div>
      <div class="modal-footer">
        <button @click="searchKey()" class="btn btn-outline-secondary" type="button" id="searchProduct" data-dismiss="modal">Search</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="createBotton" tabindex="-1" role="dialog">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <form @submit.prevent>
        <div class="modal-body">
            <div class="form-group">
              <label>商品名稱</label>
              <input class="form-control" name="newName" v-model="arr.name">
            </div>
            
            <label for="exampleInputPassword1">商品圖片</label>


            <div class="input-group">
              <div class="input-group-prepend">
                <div class="input-group-text">https://</div>
              </div>
              <input type="text" class="form-control" name="imageUrl" v-model="arr.img_url">
            </div>

            <!-- 是不是傻狗阿 -->
            
            <div class="form-group">
              <label for="exampleInputPassword1">商品價錢</label>
              <input class="form-control" name="price" v-model="arr.price">
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">商品細節</label>
              <textarea name="detail" rows="5" class="form-control" v-model="arr.detail"></textarea>
            </div>
        </div>
        <div class="modal-footer">
          <button @click="createProduct()" type="submit" class="btn btn-primary" data-dismiss="modal">新增</button>
        </div>
      </form>
    </div>
  </div>
</div>

</template>

<script>
// 搜尋功能
export default {
  name: "Nav",
  data() {
    return {
      num:0,
      arr:{
        name: "",
        price:0,
        detail: "",
        img_url:""
      },
      key: "",
    }
  },
  watch:{
  },
  computed: {
    buy: function () {
      return this.num
    },
    adminshow: function(){
      return localStorage.userid=="admin"
    },
    isAdmin: function () {
      if(this.$route.name == 'Admin') return "disabled"
      else return ""
    },
  },
  methods: {
    checkstate(){
      console.log("checkstate")
      console.log("USER:",localStorage.userid)
      if(localStorage.userid == ""){
        console.log("state= 未登入")
        return true
      }
      else{
        console.log("state= 已登入")
        return false
      }
    },
    searchKey(){
      this.$emitter.emit('keyword',this.key)
      this.key= ""
    },
    backhome(){
      var elements = document.getElementsByClassName('modal-backdrop');
      var p = elements[0].parentNode
      p.removeAttribute("style")
      p.removeAttribute("class")
      p.removeChild(elements[0])
    },
    logout(){
      this.num=0
      localStorage.userid=null
      this.$router.push("Index")
    },
    createProduct(){
      console.log(this)
      this.$http.get('http://localhost:8000/new/' + this.arr.name + '/' + this.arr.price  + '/' + this.arr.detail + '/' + this.arr.img_url)
      .then( () => this.$emitter.emit('reload',1))
      .catch( r => console.log(r))

      this.arr.name= ""
      this.arr.price= 0
      this.arr.detail= ""
      this.img_url=""
    }
  },
  mounted(){
    console.log("NAV ID=",localStorage.userid)
    this.$emitter.on('cartNum',()=>{
      this.num++
      console.log(this.num)
    })
  },
};
</script>


<style scoped>
.windowset{
  margin: 0 auto;
  max-width: 100%;
  padding: 0 0 0 0;
}
.windowset1{
  padding-right: 0 !important;
}
.windowset2{
  border-radius: 0%;
}
</style>