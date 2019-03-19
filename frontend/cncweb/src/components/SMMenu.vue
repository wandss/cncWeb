<template>
  <transition name="smMenuSlide">
    <div v-show="show">
      <div id="menu-sm">
        <h6 v-for="item in items" :key="item.name" @click="$emit('click',item.event)">
          <span v-if="item.icon" :class="item.icon">
          </span>
          {{item.name}}
        </h6>
      </div>
    </div>
  </transition>
</template>
<script>
export default{
    name:"SmMenu",
    props:{
        show:{
            type:Boolean,
            default:false
        },
        items:{
            type:Array,
            default:()=>[]
        }
    },
}
</script>
<style scoped>
#menu-sm{
    z-index:999999;
    color:#EEE;
    background-color:#6c757d;
    position:fixed;
    width:100%;
    overflow:hidden;
    padding-left:2rem;
    padding-top:1rem;
    padding-bottom:1rem;
    border-top:1px solid #666;
}
.smMenuSlide-enter-active, .smMenuSlide-leave-active{
    transition:all .3s;
}
.smMenuSlide-enter, .smMenuSlide-leave-to{
    opacity:0;
    max-height:-1rem;
    transform:translateY(-3rem);
}
</style>
