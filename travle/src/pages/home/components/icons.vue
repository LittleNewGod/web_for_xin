<template>
  <div class="icons">
      <swiper :options="swiperOption">
          <swiper-slide v-for="(page, index) of pages" :key="index">
            <div class="icon" v-for="item of page" :key="item.id">
              <div class="icon-img" >
                <img class="icon-img-content" :src="item.imgUrl" />
              </div>
              <p class="icon-desc">{{item.desc}}</p>
            </div>
          </swiper-slide>
      </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeIcons',
  data () {
    return {
      swiperOption: {
        autoplay: false
      }
      // iconList: [{
      //   id: '001',
      //   imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/95/f3dd6c383aeb3b02.png',
      //   desc: '景点门票'
      // }, {
      //   id: '002',
      //   imgUrl: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/f0f00d6dfe038c044dbc9a437f58b0eb.png',
      //   desc: '一日游'
      // }, {
      //   id: '003',
      //   imgUrl: 'http://img1.qunarzz.com/piao/fusion/1804/ff/fdf170ee89594b02.png',
      //   desc: '北京必游'
      // }, {
      //   id: '004',
      //   imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/3e/86314b2af03b7502.png',
      //   desc: '水上乐园'
      // }, {
      //   id: '005',
      //   imgUrl: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20191/0334cf5430b9b5505fd79e2b8d7e8670.png',
      //   desc: '爬长城'
      // }, {
      //   id: '006',
      //   imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/6c/9e54a8540fee0102.png',
      //   desc: '故宫'
      // }, {
      //   id: '007',
      //   imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/76/eb88861d78fb9902.png',
      //   desc: '动植物园'
      // }, {
      //   id: '008',
      //   imgUrl: 'http://img1.qunarzz.com/piao/fusion/1805/3a/754b47f658e9c602.png',
      //   desc: '怀北漂流'
      // }, {
      //   id: '009',
      //   imgUrl: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/338c5b924c5809e8c7b14f60a953c3e2.png',
      //   desc: '北京欢乐谷'
      // }]
    }
  },
  props: {
    list: Array
  },
  computed: {
    pages () {
      const pages = []
      this.list.forEach((item, index) => {
        const page = Math.floor(index / 8)
        if (!pages[page]) {
          pages[page] = []
        }
        pages[page].push(item)
      })
      return pages
    }
  }
}
</script>
<style lang='stylus' scoped>
 @import '~styles/varibles.styl'
 @import '~styles/mixins.styl'
 .icons >>> .swiper-container
   height : 0
   padding-bottom : 50%
 .icons
   margin-top : .1rem
   .icon
     position : relative
     overflow : hidden
     float : left
     width : 25%
     height : 0
     padding-bottom : 25%
     .icon-img
       position : absolute
       top : 0
       left : 0
       right : 0
       bottom : .44rem
       box-sizing: border-box
       padding : .1rem
       .icon-img-content
         height : 100%
         display : block
         margin : 0 auto
      .icon-desc
        position : absolute
        bottom  : 0
        left : 0
        right : 0
        height  : .44rem
        line-height : .44rem
        color : $darkTextColor
        text-align : center
        ellipsis()
</style>
