// import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

// function App() {
//   return <h1>Project Client</h1>;
// }



// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Layout from './Layout';
import Home from './Home';
import Artists from './Artists';
import Museums from './Museums';
import Login from './Login';
import Signup from './Signup';

function App() {
  return (
    <Router>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/artists" component={Artists} />
          <Route path="/museums" component={Museums} />
          <Route path="/login" component={Login} />
          <Route path="/signup" component={Signup} />
          {/* Add more routes for other sections */}
        </Switch>
      </Layout>
    </Router>
  );
}

export default App;

