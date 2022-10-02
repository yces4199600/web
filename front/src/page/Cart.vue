<template>

<div class="container">
  <div class="card text-white bg-dark mb-3 pad5">
    <!-- 範例卡片 -->
    <div class="row g-0" style = "border:8px #343a40 solid;" v-for="(item,index) in itemList" :key="item.id" :id="'card-' + item.id">
      <div class="col-md-4">
        <img :src="'https://' + item.img_url" class="card-img-top" alt="瑪利歐派對 超級巨星"/>
      </div>
      <div class="col-md-8" >
        <div class="card-body">
          <h5 class="card-title">{{ item.name }}</h5>
          <a class="id" style="display: none">{{ item.id }}</a>
          <p class="card-text">{{ item.detail }}</p>
          <p>訂購數量：{{cartItems[index].hitTimes}}</p>
          <button @click="remove(item.id)" class="btn btn-primary me-md-2 btn-danger">移除此商品</button>

        </div>
      </div>
    </div>
    <router-link @click="clear()" to="/"  class="btn btn-primary me-md-2 btn-success">送出訂單</router-link>
  </div>
</div>
</template>

<script>

export default {
  name: "Cart",
  data() {
    return {
      arr: [],
      cartItems: [],
      getId: [],
      currentcard:'',
    }
  },
  computed: {
    itemList: function () {
      return this.arr
    }
  },
  components: {

  },
  mounted(){
    this.getCartData()

    // console.log(this.cartItems)
  },
  methods: {
    getCartData(){
      if(localStorage.cartItems){
        this.cartItems = JSON.parse(localStorage.cartItems)
        for(let i=0;i<Object.keys(this.cartItems).length;i++){
          console.log("thiscard",this.cartItems[i].id)
          this.getId.push(this.cartItems[i].id)
        }
        this.$http.get('http://localhost:8000/cartdata'+'/'+ this.getId)
          .then( r => this.arr = r.data)
          .catch()
      }
    },
    remove(id){
      const find = document.getElementById('card-' + id)
      console.log(find)
      find.style.display = "none"
    },
    clear(){
      localStorage.cartItems = "";
      console.log(localStorage.cartItems)
      this.$router.push({name:'admin', params: { USER:localStorage.userid }})
      alert("訂單已送出！")
      // this.$route.params.USER
    }
  },

}
</script>

<style scoped>
.card{overflow:hidden;}
.card img{transform:scale(1,1);transition: all 0.5s ease-out;}
.card img:hover{transform:scale(1.1,1.1);}
.pad5{padding-left:5px;padding-right:5px;padding-bottom:5px;}
</style>