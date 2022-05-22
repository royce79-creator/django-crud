# Django CRUD - Lab 28

## Author: Connor Boyce

Version: 1.0.0 (PR URL: [PR URL](https://github.com/bran2miz/django-crud/pull/1)

## Overview

This lab assignment required us add full CRUD functionality, building a Django project that allows, Creating, Reading, Updating, and Deleting.

## Getting Started

### Lab 28

We had to create a project that followed the same steps as the previous lab, only this time we had to create CRUD functionality. We had to create a:

- SnackListView that extends appropriate generic view
associated url path is an empty string

- SnackDetailView that extends appropriate generic view
associated url path is <int:pk>/

- SnackCreateView that extends appropriate generic view
associated url path is create/

- SnackUpdateView that extends appropriate generic view
associated url path is <int:pk>/update/

- SnackDeleteView that extends appropriate generic view
associated url path is <int:pk>/delete/

We had to also add:

- urls to support all views, with appropriate names

- templates to support all views

- Add navigation links in appropriate locations to access all pages

- Make all necessary changes to project level files for project to run

- Write tests

- Add CSS

## Architecture

Python, Django, Models, get_user_model, superuser, CRUD, CSS, static.

## Change Log

03-05-22 -- All tests are passing and the assignment is complete. Added CSS for a pop of color.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Brandon Mizutani

Roger Huba
