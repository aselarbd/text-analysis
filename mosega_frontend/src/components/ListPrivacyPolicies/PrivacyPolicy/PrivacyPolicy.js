import React from 'react';
import styles from './PrivacyPolicy.css'

const privacyPolicy = (props) => {
    return (
        <div>
            <textarea className={styles.custom_textarea}
                      disabled={true}
                      value={JSON.stringify(props.policy, undefined, 4) }>
            </textarea>
        </div>
    );
};

export default privacyPolicy;