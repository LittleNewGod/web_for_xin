<template>
  <div>
    <div class="title">周末去哪儿</div>
    <ul>
      <li class="item border-bottom" v-for="item of list" :key="item.id">
        <div class="item-img-warper">
          <img class="item-img" :src="item.imgUrl" />
        </div>
        <div class="item-info">
          <p class="item-title">{{item.title}}</p>
          <p class="item-desc">{{item.desc}}</p>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: 'HomeWeekend',
  props: {
    list: Array
  }
//   data () {
//     return {
//       recommendList: [{
//         id: '001',
//         imgUrl: 'http://img1.qunarzz.com/sight/source/1811/f3/86173f863bef61.jpg_r_640x214_52b003ac.jpg',
//         title: '京城周末撒欢',
//         desc: '在帝都过周末，不仅仅是城中游！'
//       }, {
//         id: '002',
//         imgUrl: 'http://img1.qunarzz.com/sight/source/1811/7e/476589267ebb41.jpg_r_640x214_bf599709.jpg',
//         title: '京城溜娃必去',
//         desc: '德智体美劳全面发展的亲子日，这些地方该去看看…'
//       }, {
//         id: '003',
//         imgUrl: 'http://img1.qunarzz.com/sight/source/1505/aa/7baaf8a851d221.jpg_r_640x214_1431200f.jpg',
//         title: '帝都必打卡',
//         desc: '来北京必去的景点非这些地方莫属'
//       }]
//     }
//   }
}
</script>
<style lang="stylus" scoped>
@import '~styles/mixins.styl'
 .title
   line-height : .8rem
   background : #eeeeee
   text-indent : .2rem
 .item-img-warper
   overflow : hidden
   height : 0
   padding-bottom : 37.02%
   .item-img
     width : 100%
 .item-info
   padding : .1rem
   min-width : 0
   .item-title
    line-height : .54rem
    font-size : .32rem
    ellipsis()
   .item-desc
     line-height : .4rem
     color : #ccc
     ellipsis()
</style>
