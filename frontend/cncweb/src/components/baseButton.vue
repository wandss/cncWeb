<template>
  <button :class="['btn '+cssClass+' mb-1', {'btnShadow':hasShadow}]"
    @click="$emit('click')">
    <span :class="icon" v-if="icon!==undefined"></span>
    <slot></slot>
  </button>
</template>
<script>
export default{
  name:'BaseButton',
  props:{
    cssClass:{
      type:String,
      default:'btn-primary',
    },
    icon:{
      type:String,
    },
    hasShadow: {
      type: Boolean,
      default: true,
    }
  }
}
</script>
<style scoped>
.btn{
  margin-right:10px;
}
.btnShadow{
  box-shadow:1px 2px 5px 1px rgba(100, 100, 100, 1);
}
</style>
