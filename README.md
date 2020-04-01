# Term Project – Backend System for Disaster Site Resources Locator Phase I – Conceptual Design (Based on the PartsApp example in class)
Created by Roberto Hernandez, Blas Ayala and Nashali Rivera

It was designed, implemented and tested the backend of an application used to manage resources on a Disaster Site, such as Puerto Rico after hurricane Maria, or the 2020 Guanica Earthquakes. The data in the application is managed by a relational database system, and exposed to client applications through a REST API. It was developed on Pycharm.

It contains five tables:
1.Items
2.Inventory
3.Person
4.Privileges
5.Cards

And an ER Model representing the relationship between them. It also supports the following operations: 
1. Register as a system administrator. 
2. Register as a person in need of resources. 
3. Register as a person that supplies resources.  
4. Add a request for a given resource 
5. Announce the availability of a resource. 
6. Reserve or purchase a resource. Free resources are reserved.  Otherwise, they are purchased. 
7. Browse resources being requested 
8. Browse resources available 
9. See detail of resources, including location on a Google Map 
10. Keyword search resources being requested, with sorting by resource name 
11. Keyword search resources available, with sorting by resource name 
12. Show dashboard page with daily statistics on  a. Resources in need b. Resources available c. Matching between need and availability 13. Show dashboard page with trending statics (7 day period) on a. Resources in need b. Resources available c. Matching between need and availability 
14. Show dashboard page with trending statics (8 Senate Regions in PR) on a. Resources in need b. Resources available 
c. Matching between need and availability 

