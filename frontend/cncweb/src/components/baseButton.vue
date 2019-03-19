<template>
    <button :class="'btn '+cssClass+' mb-3'" @click="$emit('click')">
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
    }
}
</script>
<style scoped>
.btn{
    box-shadow:1px 2px 5px 1px rgba(100, 100, 100, 1);
    margin-right:10px;
}
</style>
