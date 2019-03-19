<template>
    <modal :show="show" @click="$emit('close')"
     :title="title">
        <div slot="body">
            <h5>{{message}}</h5>
        </div>
        <div slot="footer">
            <button class="btn btn-outline-success mx-2"
             @click="$emit('getConfirmation', true)">
               Yes
            </button>
            <button class="btn btn-outline-danger mx-2"
             @click="$emit('getConfirmation', false)">
                No
            </button>
        </div>
    </modal>
</template>
<script>
import Modal from "@/components/Modal";
export  default{
    name:'ModalConfirm',
    components:{Modal},
    props:{
        show:{
            type:Boolean,
            default:false,
            required:true,
        },
        message:{
            type:String,
            default:'Tem certeza?',
            required:true,
        },
        title:{
            type:String,
            default:'Confirm',
        },
    },
}
</script>
<style>
</style>
