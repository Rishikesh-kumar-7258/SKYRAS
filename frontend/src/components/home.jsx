import React, { useState, useEffect } from 'react'
import Footer from './footer';
import Header from './header'
import Kisaan from '../images/farmer.jpg'
import { Link } from 'react-router-dom';

const Home = () => {

    // const [schemes, setschemes] = useState();

    // useEffect(() => {
    //     fetch('http://localhost:8000/schemes')
    //         .then(res => res.json())
    //         .then(data => {
    //             setschemes(data);
    //         })
    // }, [])


    return (
        <div className="container-fluid">
            <Header />
            <div id="carouselExampleControls" className="carousel slide" data-bs-ride="carousel">
                <div className="carousel-inner">
                    <div className="carousel-item active">
                        <img src={Kisaan} className='img-fluid' alt="Kisaan" />
                    </div>
                    <div className="carousel-item">
                        <img src={Kisaan} className='img-fluid' alt="Kisaan" />
                    </div>
                    <div className="carousel-item">
                        <img src={Kisaan} className='img-fluid' alt="Kisaan" />
                    </div>
                </div>
                <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>

            <div className="row">
                <div className="col">
                    <button className="btn-yellow p-2 rounded px-5 offset-md-2 transform-up">Upload Scheme</button>
                </div>
            </div>
            <div className="container mt-3">
                <div className="row">
                    <div className="col-12 col-md-8">

                        <table className="table border table-info table-striped">
                            <thead>
                                <tr>
                                    <th scope="col">SN.</th>
                                    <th scope="col"></th>
                                    <th scope="col">Launch Date</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="col">1.</th>
                                    <th scope="col"><Link to="/scheme">First</Link></th>
                                    <th scope="col">1-2-3</th>
                                </tr>
                                <tr>
                                    <th scope="col">2.</th>
                                    <th scope="col"><Link to="/scheme">Second</Link></th>
                                    <th scope="col">2-3-4</th>
                                </tr>
                            </tbody>
                            {/* <RenderSchemes schemes={schemes}/> */}

                        </table>
                        <div className="row">
                            <div className="col-12">
                                <button className="btn-yellow w-100 p-2">Load more</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <Footer />

        </div>
    )
}

const RenderSchemes = (props) => {
    return (
        <tbody>
            {props.schemes.map((scheme, index) => {
                return (
                    <tr key={index}>
                        <th scope="row">{index + 1}</th>
                        <td><Link to="/">{scheme.name}</Link></td>
                        <td>{scheme.launchDate}</td>
                    </tr>
                )
            })}
        </tbody>
    )
}

export default Home