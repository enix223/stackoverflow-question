--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.5
-- Dumped by pg_dump version 9.5.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = stage, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: mytable; Type: TABLE; Schema: stage; Owner: so
--

CREATE TABLE mytable (
    id integer NOT NULL,
    customer_nm character varying(255)
);


ALTER TABLE mytable OWNER TO so;

--
-- Name: mytable_id_seq; Type: SEQUENCE; Schema: stage; Owner: so
--

CREATE SEQUENCE mytable_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mytable_id_seq OWNER TO so;

--
-- Name: mytable_id_seq; Type: SEQUENCE OWNED BY; Schema: stage; Owner: so
--

ALTER SEQUENCE mytable_id_seq OWNED BY mytable.id;


--
-- Name: id; Type: DEFAULT; Schema: stage; Owner: so
--

ALTER TABLE ONLY mytable ALTER COLUMN id SET DEFAULT nextval('mytable_id_seq'::regclass);


--
-- Data for Name: mytable; Type: TABLE DATA; Schema: stage; Owner: so
--

COPY mytable (id, customer_nm) FROM stdin;
1	123
\.


--
-- Name: mytable_id_seq; Type: SEQUENCE SET; Schema: stage; Owner: so
--

SELECT pg_catalog.setval('mytable_id_seq', 1, true);


--
-- Name: mytable_pkey; Type: CONSTRAINT; Schema: stage; Owner: so
--

ALTER TABLE ONLY mytable
    ADD CONSTRAINT mytable_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

