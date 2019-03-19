<template>
  <transition name="toggle">
    <div class="card mb-3" v-if="show">
      <div :class="['card-header', cssClass]" v-if="header">
        <button class="close" type="button" v-if="hasCloseBtn"
            id="close" @click="$emit('close')">
            <span aria-hidden="true">&times;</span>
        </button>
        {{header}}
      </div>
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
        <slot name="content"></slot>
      </div>
      <div class="card-footer text-muted" v-if="hasFooter">
        <slot name="footer">
        </slot>
      </div>
    </div>
  </transition>
</template>
<script>
export default{
  name:'card',
  props:{
    header:{
      type:String,
    },
    title:{
      type:String,
    },
    show:{
      type:Boolean,
      default:true,
      required:true,
    },
    hasCloseBtn:{
      type:Boolean,
      default:false,
    },
    hasFooter:{
      type:Boolean,
      default:false,
    },
    cssClass:{
      type:String,
      default:'light'
    }
  }

}
</script>
<style scoped>
#close{
  outline:none;
}
.toggle-enter-active, .toggle-leave-active{
  transition:all .5s;
}
.toggle-enter, .toggle-leave-to{
  opacity:0;
  transform:rotateY(90deg);
}
.primary{
  background-color:rgba(0, 123, 255, .9);
  color:white;
}
.secondary{
  background-color:rgba(100, 117, 125, .9);
  color:white;
}
.success{
  background-color:rgba(40, 167, 69, .9);
  color:white;
}
.danger{
  background-color:rgba(220, 53, 69, .9);
  color:white;
}
.warning{
  background-color:rgba(255, 193, 7, .9);
  color:black;
}
.info{
  background-color:rgba(23, 162, 184, .9);
  color:white;
}
.light{
  background-color:rgba(248, 249, 250, .9);
  color:black;
}
.dark{
  background-color:rgba(52, 58, 64, .9);
  color:white;
}
.white{
  background-color:rgba(255, 255, 255, .9);
  color:black;
}
</style>
