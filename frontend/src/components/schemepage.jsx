import React from 'react'
import Header from './header'
import { Link } from 'react-router-dom'

const SchemePage = () => {
    return (
        <div className="container-fluid">
            <Header />
            <Details scheme={"something"} />
            <UserList users={[{ name: 'John', age: '20' }, { name: 'Jane', age: '30' }]} />
        </div>
    )
}

const Details = (props) => {
    return (
        <div className="container">
            <div className="display-4 text-center mt-3">Scheme details</div>
            <div className="row">
                <div className="display-1 text-center">{props.scheme.title}</div>
                <p>{props.scheme.desc}</p>
                <p>{props.scheme.eligiblity}</p>
            </div>
            <div className="row">
                <div className="col-md-4 col-12 text-center border p-3">
                    <h4>Number of Eligible candidates</h4>
                    <p>{props.scheme.eligible}</p>
                </div>
                <div className="col-md-4 col-12 text-center border p-3">
                    <h4>Number of registration</h4>
                    <p>{props.scheme.registered}</p>
                </div>
                <div className="col-md-4 col-12 text-center border p-3">
                    <h4>Total benefitted</h4>
                    <p>{props.scheme.benefitted}</p>
                </div>
            </div>
        </div>
    )
}

const UserList = () => {
    return (
        <div className="container mt-5">
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
                        <th scope="col"><Link to="/profile">First</Link></th>
                        <th scope="col">1-2-3</th>
                    </tr>
                    <tr>
                        <th scope="col">2.</th>
                        <th scope="col"><Link to="/profile">Second</Link></th>
                        <th scope="col">2-3-4</th>
                    </tr>
                </tbody>
                {/* <RenderSchemes schemes={schemes}/> */}

            </table>
        </div>
    )
}

export default SchemePage