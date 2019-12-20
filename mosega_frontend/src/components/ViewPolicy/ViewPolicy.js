import React, {Component} from 'react';
import { Accordion, Icon } from 'semantic-ui-react'
import PolicyItem from "./PolicyItem";
import Aux from "../../hoc/Aux"

const flatten = require('flat');


class ViewPolicy extends Component{


    state = {
        policies: null
    }

    policyItemList="";


    restructJson (json) {

        let UIElement =[];

        let oneCycle = false;
        let newItem ={};
        let index = 0;

        for (let key in json){

            let keyContent = key.split(".");

            if (keyContent.includes("heading")){
                newItem['head'] =json[key];
            }

            if (keyContent.includes("text")){
                newItem['text'] = json[key];
                oneCycle = true;
            }

            if (oneCycle){
                newItem['index'] = index;
                UIElement.push(newItem);

                index += 1;
                newItem = {};
                oneCycle = false;
            }

        }
        return UIElement
    }


    componentDidMount() {

        const objs  = flatten(this.props.location.state);

        this.state.policy= objs;


        let items = [...this.restructJson(objs)];

        // for(let item in items){
        //     this.policyItemList += <PolicyItem
        //         key = {items[item]["index"]}
        //         heading ={items[item]["head"]}
        //         text = {items[item]["text"]}
        //         index={items[item]["index"]}
        //     />
        //     console.log(items[item]["head"])
        // }

        // items.map(
        //     item => (
        //         console.log(item["head"])
        //     )
        // );


        this.policyItemList = items.map(
            item => {
                console.log(item["head"]);

                return <PolicyItem
                    key = {item["index"]}
                    heading ={item["head"]}
                    text = {item["text"]}
                    index={item["index"]}
                />
    }
        );

        console.log(this.policyItemList);

    }





    render() {
        return (
            <Aux>

                <p>test</p>

                    {this.policyItemList}


            </Aux>
        );
    }
}

export default ViewPolicy;