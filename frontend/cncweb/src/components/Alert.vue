<template>
    <transition name="dismiss">
        <div class="row" v-show="show" id="alert">
            <div class="col-sm-12">
                <div :class="['alert', 'alert-'+cssClass]">
                    <button v-if="hasCloseBtn" class="close" type="button"
                     id="close" @click="$emit('close')"
                    >×</button>
                    <h4 v-if="title">
                        <i :class="icon"></i>
                        {{title}}
                    </h4>
                    <slot></slot>
                </div>
            </div>
        </div>
    </transition>
</template>
<script>
    export default{
        name:'Alert',
        props:{
            cssClass:{
                type:String,
                default:'success',
            },
            title:{
                type:String,
                default:'Crie um Título',
            },
            icon:{
                type:String,
            },
            show:{
                type:Boolean,
                required:true,
                default:false,
            },
            hasCloseBtn:{
                type:Boolean,
                default:false,
            }
        },
    }
</script>
<style>
.dismiss-enter, .dismiss-leave-to{
    opacity: 0;
}
.dismiss-enter-active, .dismiss-leave-active{
    transition:opacity .5s;
}
#close{
    outline:none;
}
#alert{
    width:100%;
    position:absolute;
    z-index:999999;
}
</style>
