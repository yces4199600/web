<template>

<!-- TODO: -->
<!-- 新增商品的按鈕，和彈出視窗 -->
  <div class="container">
    <div class="mt-3 row pad20">
      <!-- <div class="card col-4">
        <img src="https:%2F/f.ecimg.tw/items/DGBJCWA900BL03D/000001_1635130622.jpg" class="card-img-top" alt="瑪利歐派對 超級巨星"/>
        <div class="card-body">
          <h5 class="card-title">瑪利歐派ss對 超級巨22星</h5>
          <a class="id" style="display: none">14</a>
          <p class="card-text">
            《瑪利歐派對 超級巨星》中包含從歷代《瑪利歐派對》中嚴選出來的「雙陸遊戲」以及「小遊戲」。雙陸遊戲：如「碧姬公主的生日蛋糕」和「太空樂園」等。
          </p>
          <a href="#" class="btn btn-primary me-md-2">1790</a>
          <a href="modifyFile" class="btn btn-danger">修改</a>
        </div>
      </div> -->

      <!-- 範例卡片 -->
      <div class="card col-4" v-for="item in itemList" :key="item.id">
        <img :src="'https://' + item.img_url" class="card-img-top" alt="image not found"/>
          <div class="card-body">
          <h5 class="card-title">{{ item.name }}</h5>
          <a class="id" style="display: none">{{ item.id }}</a>
          <p class="card-text">{{ item.detail }}</p>
          <button @click="plus(item.id)" class="btn btn-success me-md-2">{{ item.price }}</button>

          <!-- <a href="modifyFile" class="btn btn-danger">修改</a> -->

            <!-- 按鈕開頁面 -->
          <button type="button" class="btn btn-danger" data-toggle="modal" :data-target="'#card-' + item.id" v-if="show">
            編輯
          </button>
        </div>

        <!-- Modal -->
        <div class="modal fade" :id="'card-' + item.id" tabindex="-1" role="dialog">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <form :id="'form-' + item.id">
                <div class="modal-body">
                    <div class="form-group">
                      <label>商品名稱</label>
                      <input class="form-control" name="oldName" type="text" :placeholder="item.name" readonly>
                      <input class="form-control" name="newName" :value="item.name">
                    </div>
                    <!-- <div class="form-group">
                      <label for="exampleInputPassword1">商品圖片</label>
                      <input  class="form-control" name="img_url" :value="item.img_url">
                    </div> -->
                    <div class="form-group">
                      <label for="exampleInputPassword1">商品價錢</label>
                      <input class="form-control" name="price" :value="item.price">
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">商品細節</label>
                      <textarea name="detail" rows="5" class="form-control" :value="item.detail"></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                  <button @click="editItem(item.id)" type="submit" class="btn btn-primary" data-dismiss="modal">修改</button>
                  <button @click="deleteItem(item.id)" type="submit" class="btn btn-danger" data-dismiss="modal" >刪除</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>



</template>

<script>
export default {
  name: "Card",
  data() {
    return {
      arr: [],
      editedData: {
        oldName: '',
        newName: '',
        img_url: '',
        price: 0,
        detail: '',
      },
      cartItems: [],
    };
  },
  computed: {
    itemList: function () { return this.arr },
    show: function(){
      return localStorage.userid=="admin"
    },
  },
  components: {

  },
  mounted(){
    this.getData()
    this.$emitter.on('reload',() => this.getData())
    this.$emitter.on('keyword',key => this.searchData(key))
  },
  methods: {
    getData(){
      this.$http.get('http://localhost:8000/products')
        .then( r => this.arr = r.data)
        .catch( r => console.log(r))
    },
    searchData(key){
      this.$http.get('http://localhost:8000/search/' + key)
        .then( r => {
          if(r.data.length == 0){
            alert("查無符合項目!")
            this.getData()
          } 
          else this.arr = r.data
        })
        .catch( r => console.log(r))
    },
    plus(id){
      const findItems = this.cartItems.find(x => x.id === id)
      if(findItems){
        findItems.hitTimes++
      }else{
        console.log("not found " + id)
        const item = {
          id : id,
          hitTimes: 1
        }
        this.cartItems.push(item)
      }
      this.$emitter.emit('cartNum',1)
      if(this.cartItems){
        localStorage.cartItems = JSON.stringify(this.cartItems);
      }

    },
    editItem(id){
      // TODO:
      // 把form的資料取出後送到
      // process.env.VUE_APP_BACKEND_URL + "modifyFile"
      // 型別的部分要注意一下
      let a = document.getElementById("form-"+id).getElementsByTagName("input")
      let b = document.getElementById("form-"+id).getElementsByTagName("textarea")
      this.editedData.oldName = a[0].placeholder
      this.editedData.newName = a[1].value
      // this.editedData.img_url = a[2].value
      this.editedData.price = a[2].value
      this.editedData.detail = b[0].value

      this.$http.get('http://localhost:8000/edit/' + id +'/' + this.editedData.newName + '/'  + this.editedData.price + '/' + this.editedData.detail)
      .then( () => this.getData())
      .catch( r => console.log(r))
    },
    deleteItem(id){
      // TODO:
      // 同上但是後端還沒寫
      this.$http.get('http://localhost:8000/del/' + id)
      .then( () => this.getData())
      .catch( r => console.log(r))
    },
  }
};
</script>

<style scoped>
.card{overflow:hidden;}
.card img{transform:scale(1,1);transition: all 0.5s ease-out;}
.card img:hover{transform:scale(1.1,1.1);}
.pad20{padding-bottom:20px;}
</style>
#https:%2F%2Fim2.book.com.tw%2Fimage%2FgetImage?i=https:%2F%2Fwww.books.com.tw%2Fimg%2F001%2F085%2F54%2F0010855481.jpg&v=5e9590d4a&w=348&h=348

