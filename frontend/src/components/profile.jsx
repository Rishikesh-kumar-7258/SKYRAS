import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserCircle } from '@fortawesome/free-solid-svg-icons'
import React from 'react'
import Header from './header'

const Profile = () => {
    return (
        <div className="container-fluid">
            <Header />
            <div className="container border">

                <div className="row">
                    <div className="col-12 col-md-4 display-1">
                        <FontAwesomeIcon icon={faUserCircle} />
                        <h2>Name</h2>
                    </div>
                </div>
                <hr />
                <div className="row">
                    <div className="col-12">
                        <h3>Personal Details</h3>
                    </div>
                    <div className="col-12 col-md-6 fs-4">Full Name : <span>Rishi</span></div>
                    <div className="col-12 col-md-6 fs-4">Phone Number : <span>+91 9341421415</span></div>
                    <div className="col-12 col-md-6 fs-4">Email : <span>rishi7258prine@gmail.com</span></div>
                </div>
                <hr />
                <div className="row">
                    <div className="col-12">
                        <h3>Location</h3>
                    </div>
                    <div className="col-12">
                        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aspernatur magni nihil cum velit iure rem recusandae obcaecati dolorum, neque cumque enim dolores eum a eligendi necessitatibus, odio dolore culpa numquam!
                    </div>
                </div>
                <hr />
            </div>
        </div>

    )
}

export default Profile