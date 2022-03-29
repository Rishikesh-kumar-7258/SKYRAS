import React from 'react'
import {Link} from 'react-router-dom'

const Login = () => {
    return (
        <div className="container-fluid p-0">
            <div className="row border main-body align-items-center m-0">
                <form className="offset-md-7 col-md-4 col-12 bg-dark text-white p-3 rounded">
                    <p className="h1 text-center">Login Form</p>
                    <div className="mb-3">
                        <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                        <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"/>
                            <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                        <input type="password" className="form-control" id="exampleInputPassword1"/>
                    </div>
                    <div className="mb-3 d-flex justify-content-between">
                        <div>
                            <input type="checkbox" className="form-check-input" id="exampleCheck1"/>
                                <label className="form-check-label" htmlFor="exampleCheck1">Remember me</label>
                        </div>
                        <Link to="/" className="text-white text-decoration-none">forgot password ?</Link>
                    </div>
                    <button type="submit" className="btn w-100 p-2 btn-yellow">Register</button>
                </form>
            </div>

        </div>
    )
}

export default Login