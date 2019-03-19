export default{
    date(value){
        let pattern = /(\d{2})+(\/|-)?(\d{2})?$/

        let englishFormatPattern = /^(\d{4})-(\d{2})-(\d{2})$/;
        let brzFormatPattern = /^(\d{2})\/(\d{2})\/(\d{4})$/
        let alert = {show:false, title:'', css:''};
        let data = {value:value, alert:alert}

        const match = pattern.exec(value)
        if(!isNaN(value[value.length - 1])){
            //Ensure that value is a number
            if(match !== null){
                if(match.index === 0){
                    data.value += '/'
                }
                if(value.length > 10){
                    data.value = value.slice(0, value.length - 1)
                }
            }
        }
        else{
            data.value = value.slice(0, value.length - 1)
        }
        if(value.length===10){
            if(brzFormatPattern.exec(data.value) !==null){
                data.value = value.replace(brzFormatPattern, '$3-$2-$1')
            }

            if(!this._isValidDate(data.value)){
                data.alert = {show:true, title:'',
                    css:'danger', message:'Invalid Date'}
                data.value = '';
            }
            else{
                data.value = value.replace(englishFormatPattern, '$3/$2/$1')
            }
        }
        return data

    },
    time(value){
        let alert = {show:false, title:'', css:''};
        let data = {value:value, alert:alert}
        const pattern = /([01]+[0-9]|(2[0-3])):?([0-5][0-9])$/

        if(isNaN(value[value.length-1])&& value.length<5){
            data.value = value.slice(0, value.length-1)
            data.alert = {show:true, title:'', css:'danger',
                message:'Only Numbers'
            }
            value = value.slice(0, value.length-1)
        }
        if(value.length==2){
            data.value += ':'
        }
        if(value.length == 5 && pattern.exec(value) === null){
            data.alert = {show:true, title:'',
                css:'danger', message:'Invalid Time'}
            data.value = '';
        }
        else if(value.length > 5){
            data.value = data.value.slice(0, value.length -1)
        }
        return data
    },
    _isValidDate(value){
        const pattern = /(\d{2})(-|\/)(\d{2})(-|\/)(\d{4})/
        let validDate = new Date(value.replace(pattern, '$5-$1-$3')+'T03:00:00.000Z')

        let formatedDate = value.replace(pattern, '$3-$1-$5')
        const jsonDatePattern = /(^\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\.(\d{3})Z/

        if(validDate.toJSON() === null){
            //Access only when user are inserting values.
            validDate = new Date(value.replace(pattern, '$5-$3-$1')+'T03:00:00.000Z')
            formatedDate = value.replace(pattern, '$1-$3-$5')
        }

        if(validDate.toJSON() !== null){
            if(formatedDate !==
                validDate.toJSON().replace(jsonDatePattern, '$1-$2-$3')){
                return false
            }
            return true
        }
        return false
    }
}
