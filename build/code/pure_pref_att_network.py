# -*- coding: utf-8 -*-

#Random network generator
#input: (list of nodes, m0)
#output: list of connections

import numpy

def add_link_to_network(edges, start_airport):
        
    #get list of available end airports, so we remove the ones that already have a link
    available_end_airports = [m for m in range(edges.shape[0]) if edges[start_airport, m] != 1.]
    
    #delete the start_airport from the list of available end airports
    available_end_airports.remove(start_airport)
    
    #count the total number of for available airports
    total_links = sum([edges[k, :].sum() for k in available_end_airports])
    
    if available_end_airports:
        
        #probability distribution for the p
        p = [edges[n,:].sum() / total_links for n in available_end_airports]
        
        #pick and end airport
        end_airport = numpy.random.choice(available_end_airports, 1, replace=False, p=p)[0]
    
        #set the entries in the edge matrix for the end_airport and starting airport to 1
        edges[start_airport,end_airport] = 1
        edges[end_airport,start_airport] = 1

    else:
        
        print "something went wrong...."
        
    return edges

def generate(nodes, m0 = 1):
    
    #make a new aiports list, start with 2 random airports
    chosen_airports = numpy.random.choice(len(nodes), 2, replace=False)
    
    #start edge matrix and connect the first 2 airports
    edges = numpy.ones((2, 2))
    numpy.fill_diagonal(edges, 0)
    
    g_dynamic = list()
    
    g_fullsize = numpy.zeros((len(nodes), len(nodes)))
    g_fullsize[0:2, 0:2] = edges.astype(int) #only if start with 2 airports!!   
    g_dynamic.append(g_fullsize[:])
    
    running = True
    
    i = 0

    while running:
        
        #make new list of airports not already chosen
        available_airports = [airport for airport in nodes if airport not in chosen_airports]
        
        if available_airports:
            
            #insert new row
            edges = numpy.insert(edges,edges.shape[0], 0, axis=0)
                    
            #insert new column
            edges = numpy.insert(edges,edges.shape[1], 0, axis=1)
        
            #choose a new airport from the available airports using a uniform distribution      
            new_airport = numpy.random.choice(available_airports, 1, replace=False)[0] #[0] because it returns a 1-d array
        
            #add it to the airports list
            chosen_airports = numpy.insert(chosen_airports,len(chosen_airports), new_airport)
    
            #add new link to the network using the latest addition (so we set the optional argument) for an m0 number of links
            for i in range(m0):
                
                edges = add_link_to_network(edges, start_airport=edges.shape[0] - 1)
        else:
            
            print "We ran out of airports."
            running = False
        
        g_fullsize = numpy.zeros((len(nodes), len(nodes)))
        g_fullsize[0:len(edges), 0:len(edges)] = edges.astype(int)
        g_dynamic.append(g_fullsize[:])

        i += 1 
            
    print 'The network consists of', len(chosen_airports), 'airports with a total of', edges.sum()/2., 'routes'
    print 'The connection matrix: \n', edges
    print 'The most amount of connections:', max([edges[i, :].sum() for i in range(edges.shape[0])])
    print 'The average amount of connections:', round(edges.sum() / float(edges.shape[0]), 2)
    
    #check symmetry
    for x in range(edges.shape[0]):
        
        assert (edges[:, x].T == edges[:, x]).all()

    g = edges.astype(int)
    
    return g, g_dynamic
