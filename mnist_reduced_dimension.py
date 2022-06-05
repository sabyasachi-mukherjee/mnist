<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>mnist_reduced_dimension</title>
  <style>
    html {
      line-height: 1.5;
      font-family: Georgia, serif;
      font-size: 20px;
      color: #1a1a1a;
      background-color: #fdfdfd;
    }
    body {
      margin: 0 auto;
      max-width: 36em;
      padding-left: 50px;
      padding-right: 50px;
      padding-top: 50px;
      padding-bottom: 50px;
      hyphens: auto;
      overflow-wrap: break-word;
      text-rendering: optimizeLegibility;
      font-kerning: normal;
    }
    @media (max-width: 600px) {
      body {
        font-size: 0.9em;
        padding: 1em;
      }
      h1 {
        font-size: 1.8em;
      }
    }
    @media print {
      body {
        background-color: transparent;
        color: black;
        font-size: 12pt;
      }
      p, h2, h3 {
        orphans: 3;
        widows: 3;
      }
      h2, h3, h4 {
        page-break-after: avoid;
      }
    }
    p {
      margin: 1em 0;
    }
    a {
      color: #1a1a1a;
    }
    a:visited {
      color: #1a1a1a;
    }
    img {
      max-width: 100%;
    }
    h1, h2, h3, h4, h5, h6 {
      margin-top: 1.4em;
    }
    h5, h6 {
      font-size: 1em;
      font-style: italic;
    }
    h6 {
      font-weight: normal;
    }
    ol, ul {
      padding-left: 1.7em;
      margin-top: 1em;
    }
    li > ol, li > ul {
      margin-top: 0;
    }
    blockquote {
      margin: 1em 0 1em 1.7em;
      padding-left: 1em;
      border-left: 2px solid #e6e6e6;
      color: #606060;
    }
    code {
      font-family: Menlo, Monaco, 'Lucida Console', Consolas, monospace;
      font-size: 85%;
      margin: 0;
    }
    pre {
      margin: 1em 0;
      overflow: auto;
    }
    pre code {
      padding: 0;
      overflow: visible;
      overflow-wrap: normal;
    }
    .sourceCode {
     background-color: transparent;
     overflow: visible;
    }
    hr {
      background-color: #1a1a1a;
      border: none;
      height: 1px;
      margin: 1em 0;
    }
    table {
      margin: 1em 0;
      border-collapse: collapse;
      width: 100%;
      overflow-x: auto;
      display: block;
      font-variant-numeric: lining-nums tabular-nums;
    }
    table caption {
      margin-bottom: 0.75em;
    }
    tbody {
      margin-top: 0.5em;
      border-top: 1px solid #1a1a1a;
      border-bottom: 1px solid #1a1a1a;
    }
    th {
      border-top: 1px solid #1a1a1a;
      padding: 0.25em 0.5em 0.25em 0.5em;
    }
    td {
      padding: 0.125em 0.5em 0.25em 0.5em;
    }
    header {
      margin-bottom: 4em;
      text-align: center;
    }
    #TOC li {
      list-style: none;
    }
    #TOC ul {
      padding-left: 1.3em;
    }
    #TOC > ul {
      padding-left: 0;
    }
    #TOC a:not(:hover) {
      text-decoration: none;
    }
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    span.underline{text-decoration: underline;}
    div.column{display: inline-block; vertical-align: top; width: 50%;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    ul.task-list{list-style: none;}
    pre > code.sourceCode { white-space: pre; position: relative; }
    pre > code.sourceCode > span { display: inline-block; line-height: 1.25; }
    pre > code.sourceCode > span:empty { height: 1.2em; }
    .sourceCode { overflow: visible; }
    code.sourceCode > span { color: inherit; text-decoration: inherit; }
    div.sourceCode { margin: 1em 0; }
    pre.sourceCode { margin: 0; }
    @media screen {
    div.sourceCode { overflow: auto; }
    }
    @media print {
    pre > code.sourceCode { white-space: pre-wrap; }
    pre > code.sourceCode > span { text-indent: -5em; padding-left: 5em; }
    }
    pre.numberSource code
      { counter-reset: source-line 0; }
    pre.numberSource code > span
      { position: relative; left: -4em; counter-increment: source-line; }
    pre.numberSource code > span > a:first-child::before
      { content: counter(source-line);
        position: relative; left: -1em; text-align: right; vertical-align: baseline;
        border: none; display: inline-block;
        -webkit-touch-callout: none; -webkit-user-select: none;
        -khtml-user-select: none; -moz-user-select: none;
        -ms-user-select: none; user-select: none;
        padding: 0 4px; width: 4em;
        color: #aaaaaa;
      }
    pre.numberSource { margin-left: 3em; border-left: 1px solid #aaaaaa;  padding-left: 4px; }
    div.sourceCode
      {   }
    @media screen {
    pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
    }
    code span.al { color: #ff0000; font-weight: bold; } /* Alert */
    code span.an { color: #60a0b0; font-weight: bold; font-style: italic; } /* Annotation */
    code span.at { color: #7d9029; } /* Attribute */
    code span.bn { color: #40a070; } /* BaseN */
    code span.bu { } /* BuiltIn */
    code span.cf { color: #007020; font-weight: bold; } /* ControlFlow */
    code span.ch { color: #4070a0; } /* Char */
    code span.cn { color: #880000; } /* Constant */
    code span.co { color: #60a0b0; font-style: italic; } /* Comment */
    code span.cv { color: #60a0b0; font-weight: bold; font-style: italic; } /* CommentVar */
    code span.do { color: #ba2121; font-style: italic; } /* Documentation */
    code span.dt { color: #902000; } /* DataType */
    code span.dv { color: #40a070; } /* DecVal */
    code span.er { color: #ff0000; font-weight: bold; } /* Error */
    code span.ex { } /* Extension */
    code span.fl { color: #40a070; } /* Float */
    code span.fu { color: #06287e; } /* Function */
    code span.im { } /* Import */
    code span.in { color: #60a0b0; font-weight: bold; font-style: italic; } /* Information */
    code span.kw { color: #007020; font-weight: bold; } /* Keyword */
    code span.op { color: #666666; } /* Operator */
    code span.ot { color: #007020; } /* Other */
    code span.pp { color: #bc7a00; } /* Preprocessor */
    code span.sc { color: #4070a0; } /* SpecialChar */
    code span.ss { color: #bb6688; } /* SpecialString */
    code span.st { color: #4070a0; } /* String */
    code span.va { color: #19177c; } /* Variable */
    code span.vs { color: #4070a0; } /* VerbatimString */
    code span.wa { color: #60a0b0; font-weight: bold; font-style: italic; } /* Warning */
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<div id="e0ddc61c" class="cell markdown">
<p>Here are the packages we use.</p>
</div>
<div id="78e376d1" class="cell code" data-execution_count="96">
<div class="sourceCode" id="cb1"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> time</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> matplotlib <span class="im">as</span> mpl</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> matplotlib.pyplot <span class="im">as</span> plt</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> numpy <span class="im">as</span> np</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.datasets <span class="im">import</span> fetch_openml</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.model_selection <span class="im">import</span> cross_val_score</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.linear_model <span class="im">import</span> SGDClassifier</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.decomposition <span class="im">import</span> PCA</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.decomposition <span class="im">import</span> IncrementalPCA</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.svm <span class="im">import</span> SVC</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.multiclass <span class="im">import</span> OneVsRestClassifier</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.metrics <span class="im">import</span> precision_score</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.metrics <span class="im">import</span> recall_score</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.ensemble <span class="im">import</span> RandomForestClassifier</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a></span></code></pre></div>
</div>
<div id="65f4a9f8" class="cell code" data-execution_count="5">
<div class="sourceCode" id="cb2"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#mnist = fetch_openml(&#39;mnist_784&#39;) </span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>mnist <span class="op">=</span> fetch_openml(<span class="st">&#39;mnist_784&#39;</span>, version <span class="op">=</span> <span class="dv">1</span>, as_frame <span class="op">=</span> <span class="va">False</span>) <span class="co">#this as_frame = False will deliver a numpy.ndarray</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">#helps makes sense of X[0] in some_digit defintion.</span></span></code></pre></div>
</div>
<div id="5105aaa7" class="cell code" data-execution_count="6">
<div class="sourceCode" id="cb3"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>mnist</span></code></pre></div>
<div class="output execute_result" data-execution_count="6">
<pre><code>{&#39;data&#39;: array([[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]]),
 &#39;target&#39;: array([&#39;5&#39;, &#39;0&#39;, &#39;4&#39;, ..., &#39;4&#39;, &#39;5&#39;, &#39;6&#39;], dtype=object),
 &#39;frame&#39;: None,
 &#39;categories&#39;: {},
 &#39;feature_names&#39;: [&#39;pixel1&#39;,
  &#39;pixel2&#39;,
  &#39;pixel3&#39;,
  &#39;pixel4&#39;,
  &#39;pixel5&#39;,
  &#39;pixel6&#39;,
  &#39;pixel7&#39;,
  &#39;pixel8&#39;,
  &#39;pixel9&#39;,
  &#39;pixel10&#39;,
  &#39;pixel11&#39;,
  &#39;pixel12&#39;,
  &#39;pixel13&#39;,
  &#39;pixel14&#39;,
  &#39;pixel15&#39;,
  &#39;pixel16&#39;,
  &#39;pixel17&#39;,
  &#39;pixel18&#39;,
  &#39;pixel19&#39;,
  &#39;pixel20&#39;,
  &#39;pixel21&#39;,
  &#39;pixel22&#39;,
  &#39;pixel23&#39;,
  &#39;pixel24&#39;,
  &#39;pixel25&#39;,
  &#39;pixel26&#39;,
  &#39;pixel27&#39;,
  &#39;pixel28&#39;,
  &#39;pixel29&#39;,
  &#39;pixel30&#39;,
  &#39;pixel31&#39;,
  &#39;pixel32&#39;,
  &#39;pixel33&#39;,
  &#39;pixel34&#39;,
  &#39;pixel35&#39;,
  &#39;pixel36&#39;,
  &#39;pixel37&#39;,
  &#39;pixel38&#39;,
  &#39;pixel39&#39;,
  &#39;pixel40&#39;,
  &#39;pixel41&#39;,
  &#39;pixel42&#39;,
  &#39;pixel43&#39;,
  &#39;pixel44&#39;,
  &#39;pixel45&#39;,
  &#39;pixel46&#39;,
  &#39;pixel47&#39;,
  &#39;pixel48&#39;,
  &#39;pixel49&#39;,
  &#39;pixel50&#39;,
  &#39;pixel51&#39;,
  &#39;pixel52&#39;,
  &#39;pixel53&#39;,
  &#39;pixel54&#39;,
  &#39;pixel55&#39;,
  &#39;pixel56&#39;,
  &#39;pixel57&#39;,
  &#39;pixel58&#39;,
  &#39;pixel59&#39;,
  &#39;pixel60&#39;,
  &#39;pixel61&#39;,
  &#39;pixel62&#39;,
  &#39;pixel63&#39;,
  &#39;pixel64&#39;,
  &#39;pixel65&#39;,
  &#39;pixel66&#39;,
  &#39;pixel67&#39;,
  &#39;pixel68&#39;,
  &#39;pixel69&#39;,
  &#39;pixel70&#39;,
  &#39;pixel71&#39;,
  &#39;pixel72&#39;,
  &#39;pixel73&#39;,
  &#39;pixel74&#39;,
  &#39;pixel75&#39;,
  &#39;pixel76&#39;,
  &#39;pixel77&#39;,
  &#39;pixel78&#39;,
  &#39;pixel79&#39;,
  &#39;pixel80&#39;,
  &#39;pixel81&#39;,
  &#39;pixel82&#39;,
  &#39;pixel83&#39;,
  &#39;pixel84&#39;,
  &#39;pixel85&#39;,
  &#39;pixel86&#39;,
  &#39;pixel87&#39;,
  &#39;pixel88&#39;,
  &#39;pixel89&#39;,
  &#39;pixel90&#39;,
  &#39;pixel91&#39;,
  &#39;pixel92&#39;,
  &#39;pixel93&#39;,
  &#39;pixel94&#39;,
  &#39;pixel95&#39;,
  &#39;pixel96&#39;,
  &#39;pixel97&#39;,
  &#39;pixel98&#39;,
  &#39;pixel99&#39;,
  &#39;pixel100&#39;,
  &#39;pixel101&#39;,
  &#39;pixel102&#39;,
  &#39;pixel103&#39;,
  &#39;pixel104&#39;,
  &#39;pixel105&#39;,
  &#39;pixel106&#39;,
  &#39;pixel107&#39;,
  &#39;pixel108&#39;,
  &#39;pixel109&#39;,
  &#39;pixel110&#39;,
  &#39;pixel111&#39;,
  &#39;pixel112&#39;,
  &#39;pixel113&#39;,
  &#39;pixel114&#39;,
  &#39;pixel115&#39;,
  &#39;pixel116&#39;,
  &#39;pixel117&#39;,
  &#39;pixel118&#39;,
  &#39;pixel119&#39;,
  &#39;pixel120&#39;,
  &#39;pixel121&#39;,
  &#39;pixel122&#39;,
  &#39;pixel123&#39;,
  &#39;pixel124&#39;,
  &#39;pixel125&#39;,
  &#39;pixel126&#39;,
  &#39;pixel127&#39;,
  &#39;pixel128&#39;,
  &#39;pixel129&#39;,
  &#39;pixel130&#39;,
  &#39;pixel131&#39;,
  &#39;pixel132&#39;,
  &#39;pixel133&#39;,
  &#39;pixel134&#39;,
  &#39;pixel135&#39;,
  &#39;pixel136&#39;,
  &#39;pixel137&#39;,
  &#39;pixel138&#39;,
  &#39;pixel139&#39;,
  &#39;pixel140&#39;,
  &#39;pixel141&#39;,
  &#39;pixel142&#39;,
  &#39;pixel143&#39;,
  &#39;pixel144&#39;,
  &#39;pixel145&#39;,
  &#39;pixel146&#39;,
  &#39;pixel147&#39;,
  &#39;pixel148&#39;,
  &#39;pixel149&#39;,
  &#39;pixel150&#39;,
  &#39;pixel151&#39;,
  &#39;pixel152&#39;,
  &#39;pixel153&#39;,
  &#39;pixel154&#39;,
  &#39;pixel155&#39;,
  &#39;pixel156&#39;,
  &#39;pixel157&#39;,
  &#39;pixel158&#39;,
  &#39;pixel159&#39;,
  &#39;pixel160&#39;,
  &#39;pixel161&#39;,
  &#39;pixel162&#39;,
  &#39;pixel163&#39;,
  &#39;pixel164&#39;,
  &#39;pixel165&#39;,
  &#39;pixel166&#39;,
  &#39;pixel167&#39;,
  &#39;pixel168&#39;,
  &#39;pixel169&#39;,
  &#39;pixel170&#39;,
  &#39;pixel171&#39;,
  &#39;pixel172&#39;,
  &#39;pixel173&#39;,
  &#39;pixel174&#39;,
  &#39;pixel175&#39;,
  &#39;pixel176&#39;,
  &#39;pixel177&#39;,
  &#39;pixel178&#39;,
  &#39;pixel179&#39;,
  &#39;pixel180&#39;,
  &#39;pixel181&#39;,
  &#39;pixel182&#39;,
  &#39;pixel183&#39;,
  &#39;pixel184&#39;,
  &#39;pixel185&#39;,
  &#39;pixel186&#39;,
  &#39;pixel187&#39;,
  &#39;pixel188&#39;,
  &#39;pixel189&#39;,
  &#39;pixel190&#39;,
  &#39;pixel191&#39;,
  &#39;pixel192&#39;,
  &#39;pixel193&#39;,
  &#39;pixel194&#39;,
  &#39;pixel195&#39;,
  &#39;pixel196&#39;,
  &#39;pixel197&#39;,
  &#39;pixel198&#39;,
  &#39;pixel199&#39;,
  &#39;pixel200&#39;,
  &#39;pixel201&#39;,
  &#39;pixel202&#39;,
  &#39;pixel203&#39;,
  &#39;pixel204&#39;,
  &#39;pixel205&#39;,
  &#39;pixel206&#39;,
  &#39;pixel207&#39;,
  &#39;pixel208&#39;,
  &#39;pixel209&#39;,
  &#39;pixel210&#39;,
  &#39;pixel211&#39;,
  &#39;pixel212&#39;,
  &#39;pixel213&#39;,
  &#39;pixel214&#39;,
  &#39;pixel215&#39;,
  &#39;pixel216&#39;,
  &#39;pixel217&#39;,
  &#39;pixel218&#39;,
  &#39;pixel219&#39;,
  &#39;pixel220&#39;,
  &#39;pixel221&#39;,
  &#39;pixel222&#39;,
  &#39;pixel223&#39;,
  &#39;pixel224&#39;,
  &#39;pixel225&#39;,
  &#39;pixel226&#39;,
  &#39;pixel227&#39;,
  &#39;pixel228&#39;,
  &#39;pixel229&#39;,
  &#39;pixel230&#39;,
  &#39;pixel231&#39;,
  &#39;pixel232&#39;,
  &#39;pixel233&#39;,
  &#39;pixel234&#39;,
  &#39;pixel235&#39;,
  &#39;pixel236&#39;,
  &#39;pixel237&#39;,
  &#39;pixel238&#39;,
  &#39;pixel239&#39;,
  &#39;pixel240&#39;,
  &#39;pixel241&#39;,
  &#39;pixel242&#39;,
  &#39;pixel243&#39;,
  &#39;pixel244&#39;,
  &#39;pixel245&#39;,
  &#39;pixel246&#39;,
  &#39;pixel247&#39;,
  &#39;pixel248&#39;,
  &#39;pixel249&#39;,
  &#39;pixel250&#39;,
  &#39;pixel251&#39;,
  &#39;pixel252&#39;,
  &#39;pixel253&#39;,
  &#39;pixel254&#39;,
  &#39;pixel255&#39;,
  &#39;pixel256&#39;,
  &#39;pixel257&#39;,
  &#39;pixel258&#39;,
  &#39;pixel259&#39;,
  &#39;pixel260&#39;,
  &#39;pixel261&#39;,
  &#39;pixel262&#39;,
  &#39;pixel263&#39;,
  &#39;pixel264&#39;,
  &#39;pixel265&#39;,
  &#39;pixel266&#39;,
  &#39;pixel267&#39;,
  &#39;pixel268&#39;,
  &#39;pixel269&#39;,
  &#39;pixel270&#39;,
  &#39;pixel271&#39;,
  &#39;pixel272&#39;,
  &#39;pixel273&#39;,
  &#39;pixel274&#39;,
  &#39;pixel275&#39;,
  &#39;pixel276&#39;,
  &#39;pixel277&#39;,
  &#39;pixel278&#39;,
  &#39;pixel279&#39;,
  &#39;pixel280&#39;,
  &#39;pixel281&#39;,
  &#39;pixel282&#39;,
  &#39;pixel283&#39;,
  &#39;pixel284&#39;,
  &#39;pixel285&#39;,
  &#39;pixel286&#39;,
  &#39;pixel287&#39;,
  &#39;pixel288&#39;,
  &#39;pixel289&#39;,
  &#39;pixel290&#39;,
  &#39;pixel291&#39;,
  &#39;pixel292&#39;,
  &#39;pixel293&#39;,
  &#39;pixel294&#39;,
  &#39;pixel295&#39;,
  &#39;pixel296&#39;,
  &#39;pixel297&#39;,
  &#39;pixel298&#39;,
  &#39;pixel299&#39;,
  &#39;pixel300&#39;,
  &#39;pixel301&#39;,
  &#39;pixel302&#39;,
  &#39;pixel303&#39;,
  &#39;pixel304&#39;,
  &#39;pixel305&#39;,
  &#39;pixel306&#39;,
  &#39;pixel307&#39;,
  &#39;pixel308&#39;,
  &#39;pixel309&#39;,
  &#39;pixel310&#39;,
  &#39;pixel311&#39;,
  &#39;pixel312&#39;,
  &#39;pixel313&#39;,
  &#39;pixel314&#39;,
  &#39;pixel315&#39;,
  &#39;pixel316&#39;,
  &#39;pixel317&#39;,
  &#39;pixel318&#39;,
  &#39;pixel319&#39;,
  &#39;pixel320&#39;,
  &#39;pixel321&#39;,
  &#39;pixel322&#39;,
  &#39;pixel323&#39;,
  &#39;pixel324&#39;,
  &#39;pixel325&#39;,
  &#39;pixel326&#39;,
  &#39;pixel327&#39;,
  &#39;pixel328&#39;,
  &#39;pixel329&#39;,
  &#39;pixel330&#39;,
  &#39;pixel331&#39;,
  &#39;pixel332&#39;,
  &#39;pixel333&#39;,
  &#39;pixel334&#39;,
  &#39;pixel335&#39;,
  &#39;pixel336&#39;,
  &#39;pixel337&#39;,
  &#39;pixel338&#39;,
  &#39;pixel339&#39;,
  &#39;pixel340&#39;,
  &#39;pixel341&#39;,
  &#39;pixel342&#39;,
  &#39;pixel343&#39;,
  &#39;pixel344&#39;,
  &#39;pixel345&#39;,
  &#39;pixel346&#39;,
  &#39;pixel347&#39;,
  &#39;pixel348&#39;,
  &#39;pixel349&#39;,
  &#39;pixel350&#39;,
  &#39;pixel351&#39;,
  &#39;pixel352&#39;,
  &#39;pixel353&#39;,
  &#39;pixel354&#39;,
  &#39;pixel355&#39;,
  &#39;pixel356&#39;,
  &#39;pixel357&#39;,
  &#39;pixel358&#39;,
  &#39;pixel359&#39;,
  &#39;pixel360&#39;,
  &#39;pixel361&#39;,
  &#39;pixel362&#39;,
  &#39;pixel363&#39;,
  &#39;pixel364&#39;,
  &#39;pixel365&#39;,
  &#39;pixel366&#39;,
  &#39;pixel367&#39;,
  &#39;pixel368&#39;,
  &#39;pixel369&#39;,
  &#39;pixel370&#39;,
  &#39;pixel371&#39;,
  &#39;pixel372&#39;,
  &#39;pixel373&#39;,
  &#39;pixel374&#39;,
  &#39;pixel375&#39;,
  &#39;pixel376&#39;,
  &#39;pixel377&#39;,
  &#39;pixel378&#39;,
  &#39;pixel379&#39;,
  &#39;pixel380&#39;,
  &#39;pixel381&#39;,
  &#39;pixel382&#39;,
  &#39;pixel383&#39;,
  &#39;pixel384&#39;,
  &#39;pixel385&#39;,
  &#39;pixel386&#39;,
  &#39;pixel387&#39;,
  &#39;pixel388&#39;,
  &#39;pixel389&#39;,
  &#39;pixel390&#39;,
  &#39;pixel391&#39;,
  &#39;pixel392&#39;,
  &#39;pixel393&#39;,
  &#39;pixel394&#39;,
  &#39;pixel395&#39;,
  &#39;pixel396&#39;,
  &#39;pixel397&#39;,
  &#39;pixel398&#39;,
  &#39;pixel399&#39;,
  &#39;pixel400&#39;,
  &#39;pixel401&#39;,
  &#39;pixel402&#39;,
  &#39;pixel403&#39;,
  &#39;pixel404&#39;,
  &#39;pixel405&#39;,
  &#39;pixel406&#39;,
  &#39;pixel407&#39;,
  &#39;pixel408&#39;,
  &#39;pixel409&#39;,
  &#39;pixel410&#39;,
  &#39;pixel411&#39;,
  &#39;pixel412&#39;,
  &#39;pixel413&#39;,
  &#39;pixel414&#39;,
  &#39;pixel415&#39;,
  &#39;pixel416&#39;,
  &#39;pixel417&#39;,
  &#39;pixel418&#39;,
  &#39;pixel419&#39;,
  &#39;pixel420&#39;,
  &#39;pixel421&#39;,
  &#39;pixel422&#39;,
  &#39;pixel423&#39;,
  &#39;pixel424&#39;,
  &#39;pixel425&#39;,
  &#39;pixel426&#39;,
  &#39;pixel427&#39;,
  &#39;pixel428&#39;,
  &#39;pixel429&#39;,
  &#39;pixel430&#39;,
  &#39;pixel431&#39;,
  &#39;pixel432&#39;,
  &#39;pixel433&#39;,
  &#39;pixel434&#39;,
  &#39;pixel435&#39;,
  &#39;pixel436&#39;,
  &#39;pixel437&#39;,
  &#39;pixel438&#39;,
  &#39;pixel439&#39;,
  &#39;pixel440&#39;,
  &#39;pixel441&#39;,
  &#39;pixel442&#39;,
  &#39;pixel443&#39;,
  &#39;pixel444&#39;,
  &#39;pixel445&#39;,
  &#39;pixel446&#39;,
  &#39;pixel447&#39;,
  &#39;pixel448&#39;,
  &#39;pixel449&#39;,
  &#39;pixel450&#39;,
  &#39;pixel451&#39;,
  &#39;pixel452&#39;,
  &#39;pixel453&#39;,
  &#39;pixel454&#39;,
  &#39;pixel455&#39;,
  &#39;pixel456&#39;,
  &#39;pixel457&#39;,
  &#39;pixel458&#39;,
  &#39;pixel459&#39;,
  &#39;pixel460&#39;,
  &#39;pixel461&#39;,
  &#39;pixel462&#39;,
  &#39;pixel463&#39;,
  &#39;pixel464&#39;,
  &#39;pixel465&#39;,
  &#39;pixel466&#39;,
  &#39;pixel467&#39;,
  &#39;pixel468&#39;,
  &#39;pixel469&#39;,
  &#39;pixel470&#39;,
  &#39;pixel471&#39;,
  &#39;pixel472&#39;,
  &#39;pixel473&#39;,
  &#39;pixel474&#39;,
  &#39;pixel475&#39;,
  &#39;pixel476&#39;,
  &#39;pixel477&#39;,
  &#39;pixel478&#39;,
  &#39;pixel479&#39;,
  &#39;pixel480&#39;,
  &#39;pixel481&#39;,
  &#39;pixel482&#39;,
  &#39;pixel483&#39;,
  &#39;pixel484&#39;,
  &#39;pixel485&#39;,
  &#39;pixel486&#39;,
  &#39;pixel487&#39;,
  &#39;pixel488&#39;,
  &#39;pixel489&#39;,
  &#39;pixel490&#39;,
  &#39;pixel491&#39;,
  &#39;pixel492&#39;,
  &#39;pixel493&#39;,
  &#39;pixel494&#39;,
  &#39;pixel495&#39;,
  &#39;pixel496&#39;,
  &#39;pixel497&#39;,
  &#39;pixel498&#39;,
  &#39;pixel499&#39;,
  &#39;pixel500&#39;,
  &#39;pixel501&#39;,
  &#39;pixel502&#39;,
  &#39;pixel503&#39;,
  &#39;pixel504&#39;,
  &#39;pixel505&#39;,
  &#39;pixel506&#39;,
  &#39;pixel507&#39;,
  &#39;pixel508&#39;,
  &#39;pixel509&#39;,
  &#39;pixel510&#39;,
  &#39;pixel511&#39;,
  &#39;pixel512&#39;,
  &#39;pixel513&#39;,
  &#39;pixel514&#39;,
  &#39;pixel515&#39;,
  &#39;pixel516&#39;,
  &#39;pixel517&#39;,
  &#39;pixel518&#39;,
  &#39;pixel519&#39;,
  &#39;pixel520&#39;,
  &#39;pixel521&#39;,
  &#39;pixel522&#39;,
  &#39;pixel523&#39;,
  &#39;pixel524&#39;,
  &#39;pixel525&#39;,
  &#39;pixel526&#39;,
  &#39;pixel527&#39;,
  &#39;pixel528&#39;,
  &#39;pixel529&#39;,
  &#39;pixel530&#39;,
  &#39;pixel531&#39;,
  &#39;pixel532&#39;,
  &#39;pixel533&#39;,
  &#39;pixel534&#39;,
  &#39;pixel535&#39;,
  &#39;pixel536&#39;,
  &#39;pixel537&#39;,
  &#39;pixel538&#39;,
  &#39;pixel539&#39;,
  &#39;pixel540&#39;,
  &#39;pixel541&#39;,
  &#39;pixel542&#39;,
  &#39;pixel543&#39;,
  &#39;pixel544&#39;,
  &#39;pixel545&#39;,
  &#39;pixel546&#39;,
  &#39;pixel547&#39;,
  &#39;pixel548&#39;,
  &#39;pixel549&#39;,
  &#39;pixel550&#39;,
  &#39;pixel551&#39;,
  &#39;pixel552&#39;,
  &#39;pixel553&#39;,
  &#39;pixel554&#39;,
  &#39;pixel555&#39;,
  &#39;pixel556&#39;,
  &#39;pixel557&#39;,
  &#39;pixel558&#39;,
  &#39;pixel559&#39;,
  &#39;pixel560&#39;,
  &#39;pixel561&#39;,
  &#39;pixel562&#39;,
  &#39;pixel563&#39;,
  &#39;pixel564&#39;,
  &#39;pixel565&#39;,
  &#39;pixel566&#39;,
  &#39;pixel567&#39;,
  &#39;pixel568&#39;,
  &#39;pixel569&#39;,
  &#39;pixel570&#39;,
  &#39;pixel571&#39;,
  &#39;pixel572&#39;,
  &#39;pixel573&#39;,
  &#39;pixel574&#39;,
  &#39;pixel575&#39;,
  &#39;pixel576&#39;,
  &#39;pixel577&#39;,
  &#39;pixel578&#39;,
  &#39;pixel579&#39;,
  &#39;pixel580&#39;,
  &#39;pixel581&#39;,
  &#39;pixel582&#39;,
  &#39;pixel583&#39;,
  &#39;pixel584&#39;,
  &#39;pixel585&#39;,
  &#39;pixel586&#39;,
  &#39;pixel587&#39;,
  &#39;pixel588&#39;,
  &#39;pixel589&#39;,
  &#39;pixel590&#39;,
  &#39;pixel591&#39;,
  &#39;pixel592&#39;,
  &#39;pixel593&#39;,
  &#39;pixel594&#39;,
  &#39;pixel595&#39;,
  &#39;pixel596&#39;,
  &#39;pixel597&#39;,
  &#39;pixel598&#39;,
  &#39;pixel599&#39;,
  &#39;pixel600&#39;,
  &#39;pixel601&#39;,
  &#39;pixel602&#39;,
  &#39;pixel603&#39;,
  &#39;pixel604&#39;,
  &#39;pixel605&#39;,
  &#39;pixel606&#39;,
  &#39;pixel607&#39;,
  &#39;pixel608&#39;,
  &#39;pixel609&#39;,
  &#39;pixel610&#39;,
  &#39;pixel611&#39;,
  &#39;pixel612&#39;,
  &#39;pixel613&#39;,
  &#39;pixel614&#39;,
  &#39;pixel615&#39;,
  &#39;pixel616&#39;,
  &#39;pixel617&#39;,
  &#39;pixel618&#39;,
  &#39;pixel619&#39;,
  &#39;pixel620&#39;,
  &#39;pixel621&#39;,
  &#39;pixel622&#39;,
  &#39;pixel623&#39;,
  &#39;pixel624&#39;,
  &#39;pixel625&#39;,
  &#39;pixel626&#39;,
  &#39;pixel627&#39;,
  &#39;pixel628&#39;,
  &#39;pixel629&#39;,
  &#39;pixel630&#39;,
  &#39;pixel631&#39;,
  &#39;pixel632&#39;,
  &#39;pixel633&#39;,
  &#39;pixel634&#39;,
  &#39;pixel635&#39;,
  &#39;pixel636&#39;,
  &#39;pixel637&#39;,
  &#39;pixel638&#39;,
  &#39;pixel639&#39;,
  &#39;pixel640&#39;,
  &#39;pixel641&#39;,
  &#39;pixel642&#39;,
  &#39;pixel643&#39;,
  &#39;pixel644&#39;,
  &#39;pixel645&#39;,
  &#39;pixel646&#39;,
  &#39;pixel647&#39;,
  &#39;pixel648&#39;,
  &#39;pixel649&#39;,
  &#39;pixel650&#39;,
  &#39;pixel651&#39;,
  &#39;pixel652&#39;,
  &#39;pixel653&#39;,
  &#39;pixel654&#39;,
  &#39;pixel655&#39;,
  &#39;pixel656&#39;,
  &#39;pixel657&#39;,
  &#39;pixel658&#39;,
  &#39;pixel659&#39;,
  &#39;pixel660&#39;,
  &#39;pixel661&#39;,
  &#39;pixel662&#39;,
  &#39;pixel663&#39;,
  &#39;pixel664&#39;,
  &#39;pixel665&#39;,
  &#39;pixel666&#39;,
  &#39;pixel667&#39;,
  &#39;pixel668&#39;,
  &#39;pixel669&#39;,
  &#39;pixel670&#39;,
  &#39;pixel671&#39;,
  &#39;pixel672&#39;,
  &#39;pixel673&#39;,
  &#39;pixel674&#39;,
  &#39;pixel675&#39;,
  &#39;pixel676&#39;,
  &#39;pixel677&#39;,
  &#39;pixel678&#39;,
  &#39;pixel679&#39;,
  &#39;pixel680&#39;,
  &#39;pixel681&#39;,
  &#39;pixel682&#39;,
  &#39;pixel683&#39;,
  &#39;pixel684&#39;,
  &#39;pixel685&#39;,
  &#39;pixel686&#39;,
  &#39;pixel687&#39;,
  &#39;pixel688&#39;,
  &#39;pixel689&#39;,
  &#39;pixel690&#39;,
  &#39;pixel691&#39;,
  &#39;pixel692&#39;,
  &#39;pixel693&#39;,
  &#39;pixel694&#39;,
  &#39;pixel695&#39;,
  &#39;pixel696&#39;,
  &#39;pixel697&#39;,
  &#39;pixel698&#39;,
  &#39;pixel699&#39;,
  &#39;pixel700&#39;,
  &#39;pixel701&#39;,
  &#39;pixel702&#39;,
  &#39;pixel703&#39;,
  &#39;pixel704&#39;,
  &#39;pixel705&#39;,
  &#39;pixel706&#39;,
  &#39;pixel707&#39;,
  &#39;pixel708&#39;,
  &#39;pixel709&#39;,
  &#39;pixel710&#39;,
  &#39;pixel711&#39;,
  &#39;pixel712&#39;,
  &#39;pixel713&#39;,
  &#39;pixel714&#39;,
  &#39;pixel715&#39;,
  &#39;pixel716&#39;,
  &#39;pixel717&#39;,
  &#39;pixel718&#39;,
  &#39;pixel719&#39;,
  &#39;pixel720&#39;,
  &#39;pixel721&#39;,
  &#39;pixel722&#39;,
  &#39;pixel723&#39;,
  &#39;pixel724&#39;,
  &#39;pixel725&#39;,
  &#39;pixel726&#39;,
  &#39;pixel727&#39;,
  &#39;pixel728&#39;,
  &#39;pixel729&#39;,
  &#39;pixel730&#39;,
  &#39;pixel731&#39;,
  &#39;pixel732&#39;,
  &#39;pixel733&#39;,
  &#39;pixel734&#39;,
  &#39;pixel735&#39;,
  &#39;pixel736&#39;,
  &#39;pixel737&#39;,
  &#39;pixel738&#39;,
  &#39;pixel739&#39;,
  &#39;pixel740&#39;,
  &#39;pixel741&#39;,
  &#39;pixel742&#39;,
  &#39;pixel743&#39;,
  &#39;pixel744&#39;,
  &#39;pixel745&#39;,
  &#39;pixel746&#39;,
  &#39;pixel747&#39;,
  &#39;pixel748&#39;,
  &#39;pixel749&#39;,
  &#39;pixel750&#39;,
  &#39;pixel751&#39;,
  &#39;pixel752&#39;,
  &#39;pixel753&#39;,
  &#39;pixel754&#39;,
  &#39;pixel755&#39;,
  &#39;pixel756&#39;,
  &#39;pixel757&#39;,
  &#39;pixel758&#39;,
  &#39;pixel759&#39;,
  &#39;pixel760&#39;,
  &#39;pixel761&#39;,
  &#39;pixel762&#39;,
  &#39;pixel763&#39;,
  &#39;pixel764&#39;,
  &#39;pixel765&#39;,
  &#39;pixel766&#39;,
  &#39;pixel767&#39;,
  &#39;pixel768&#39;,
  &#39;pixel769&#39;,
  &#39;pixel770&#39;,
  &#39;pixel771&#39;,
  &#39;pixel772&#39;,
  &#39;pixel773&#39;,
  &#39;pixel774&#39;,
  &#39;pixel775&#39;,
  &#39;pixel776&#39;,
  &#39;pixel777&#39;,
  &#39;pixel778&#39;,
  &#39;pixel779&#39;,
  &#39;pixel780&#39;,
  &#39;pixel781&#39;,
  &#39;pixel782&#39;,
  &#39;pixel783&#39;,
  &#39;pixel784&#39;],
 &#39;target_names&#39;: [&#39;class&#39;],
 &#39;DESCR&#39;: &quot;**Author**: Yann LeCun, Corinna Cortes, Christopher J.C. Burges  \n**Source**: [MNIST Website](http://yann.lecun.com/exdb/mnist/) - Date unknown  \n**Please cite**:  \n\nThe MNIST database of handwritten digits with 784 features, raw data available at: http://yann.lecun.com/exdb/mnist/. It can be split in a training set of the first 60,000 examples, and a test set of 10,000 examples  \n\nIt is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image. It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting. The original black and white (bilevel) images from NIST were size normalized to fit in a 20x20 pixel box while preserving their aspect ratio. The resulting images contain grey levels as a result of the anti-aliasing technique used by the normalization algorithm. the images were centered in a 28x28 image by computing the center of mass of the pixels, and translating the image so as to position this point at the center of the 28x28 field.  \n\nWith some classification methods (particularly template-based methods, such as SVM and K-nearest neighbors), the error rate improves when the digits are centered by bounding box rather than center of mass. If you do this kind of pre-processing, you should report it in your publications. The MNIST database was constructed from NIST&#39;s NIST originally designated SD-3 as their training set and SD-1 as their test set. However, SD-3 is much cleaner and easier to recognize than SD-1. The reason for this can be found on the fact that SD-3 was collected among Census Bureau employees, while SD-1 was collected among high-school students. Drawing sensible conclusions from learning experiments requires that the result be independent of the choice of training set and test among the complete set of samples. Therefore it was necessary to build a new database by mixing NIST&#39;s datasets.  \n\nThe MNIST training set is composed of 30,000 patterns from SD-3 and 30,000 patterns from SD-1. Our test set was composed of 5,000 patterns from SD-3 and 5,000 patterns from SD-1. The 60,000 pattern training set contained examples from approximately 250 writers. We made sure that the sets of writers of the training set and test set were disjoint. SD-1 contains 58,527 digit images written by 500 different writers. In contrast to SD-3, where blocks of data from each writer appeared in sequence, the data in SD-1 is scrambled. Writer identities for SD-1 is available and we used this information to unscramble the writers. We then split SD-1 in two: characters written by the first 250 writers went into our new training set. The remaining 250 writers were placed in our test set. Thus we had two sets with nearly 30,000 examples each. The new training set was completed with enough examples from SD-3, starting at pattern # 0, to make a full set of 60,000 training patterns. Similarly, the new test set was completed with SD-3 examples starting at pattern # 35,000 to make a full set with 60,000 test patterns. Only a subset of 10,000 test images (5,000 from SD-1 and 5,000 from SD-3) is available on this site. The full 60,000 sample training set is available.\n\nDownloaded from openml.org.&quot;,
 &#39;details&#39;: {&#39;id&#39;: &#39;554&#39;,
  &#39;name&#39;: &#39;mnist_784&#39;,
  &#39;version&#39;: &#39;1&#39;,
  &#39;description_version&#39;: &#39;1&#39;,
  &#39;format&#39;: &#39;ARFF&#39;,
  &#39;creator&#39;: [&#39;Yann LeCun&#39;, &#39;Corinna Cortes&#39;, &#39;Christopher J.C. Burges&#39;],
  &#39;upload_date&#39;: &#39;2014-09-29T03:28:38&#39;,
  &#39;language&#39;: &#39;English&#39;,
  &#39;licence&#39;: &#39;Public&#39;,
  &#39;url&#39;: &#39;https://old.openml.org/data/v1/download/52667/mnist_784.arff&#39;,
  &#39;file_id&#39;: &#39;52667&#39;,
  &#39;default_target_attribute&#39;: &#39;class&#39;,
  &#39;tag&#39;: [&#39;AzurePilot&#39;,
   &#39;OpenML-CC18&#39;,
   &#39;OpenML100&#39;,
   &#39;study_1&#39;,
   &#39;study_123&#39;,
   &#39;study_41&#39;,
   &#39;study_99&#39;,
   &#39;vision&#39;],
  &#39;visibility&#39;: &#39;public&#39;,
  &#39;minio_url&#39;: &#39;http://openml1.win.tue.nl/dataset554/dataset_554.pq&#39;,
  &#39;status&#39;: &#39;active&#39;,
  &#39;processing_date&#39;: &#39;2020-11-20 20:12:09&#39;,
  &#39;md5_checksum&#39;: &#39;0298d579eb1b86163de7723944c7e495&#39;},
 &#39;url&#39;: &#39;https://www.openml.org/d/554&#39;}</code></pre>
</div>
</div>
<div id="51480668" class="cell code" data-execution_count="7">
<div class="sourceCode" id="cb5"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>mnist.keys()</span></code></pre></div>
<div class="output execute_result" data-execution_count="7">
<pre><code>dict_keys([&#39;data&#39;, &#39;target&#39;, &#39;frame&#39;, &#39;categories&#39;, &#39;feature_names&#39;, &#39;target_names&#39;, &#39;DESCR&#39;, &#39;details&#39;, &#39;url&#39;])</code></pre>
</div>
</div>
<div id="291f5feb" class="cell code" data-execution_count="8">
<div class="sourceCode" id="cb7"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a>X, y <span class="op">=</span> mnist[<span class="st">&quot;data&quot;</span>], mnist[<span class="st">&quot;target&quot;</span>] </span></code></pre></div>
</div>
<div id="1623f8c8" class="cell code" data-execution_count="10">
<div class="sourceCode" id="cb8"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a>X.shape</span></code></pre></div>
<div class="output execute_result" data-execution_count="10">
<pre><code>(70000, 784)</code></pre>
</div>
</div>
<div id="fb465a41" class="cell code" data-execution_count="11">
<div class="sourceCode" id="cb10"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a>y.shape</span></code></pre></div>
<div class="output execute_result" data-execution_count="11">
<pre><code>(70000,)</code></pre>
</div>
</div>
<div id="00d29e57" class="cell code" data-execution_count="12">
<div class="sourceCode" id="cb12"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a>some_digit <span class="op">=</span> X[<span class="dv">0</span>]</span>
<span id="cb12-2"><a href="#cb12-2" aria-hidden="true" tabindex="-1"></a>some_digit_image <span class="op">=</span> some_digit.reshape(<span class="dv">28</span>,<span class="dv">28</span>)</span>
<span id="cb12-3"><a href="#cb12-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb12-4"><a href="#cb12-4" aria-hidden="true" tabindex="-1"></a>plt.imshow(some_digit_image, cmap<span class="op">=</span> <span class="st">&quot;binary&quot;</span>)</span>
<span id="cb12-5"><a href="#cb12-5" aria-hidden="true" tabindex="-1"></a>plt.axis(<span class="st">&quot;off&quot;</span>)</span>
<span id="cb12-6"><a href="#cb12-6" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img src="83465f91a3d9362e150586369ed76f1503f17f6f.png" /></p>
</div>
</div>
<div id="5006fc41" class="cell code" data-execution_count="13">
<div class="sourceCode" id="cb13"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb13-1"><a href="#cb13-1" aria-hidden="true" tabindex="-1"></a>y[<span class="dv">0</span>]</span></code></pre></div>
<div class="output execute_result" data-execution_count="13">
<pre><code>&#39;5&#39;</code></pre>
</div>
</div>
<div id="6464d8f0" class="cell code" data-execution_count="16">
<div class="sourceCode" id="cb15"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb15-1"><a href="#cb15-1" aria-hidden="true" tabindex="-1"></a>y <span class="op">=</span> y.astype(np.uint8) <span class="co">#converts y[i]&#39;s to integers</span></span></code></pre></div>
</div>
<div id="4780aa56" class="cell code" data-execution_count="17">
<div class="sourceCode" id="cb16"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a><span class="co">&quot;&quot;&quot;</span></span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a><span class="co">Split the MNIST dataset into 60000 training images and 10000 for testing. Normally, we would leave it there. </span></span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a><span class="co">But instead we do PCA.</span></span>
<span id="cb16-4"><a href="#cb16-4" aria-hidden="true" tabindex="-1"></a><span class="co">&quot;&quot;&quot;</span></span>
<span id="cb16-5"><a href="#cb16-5" aria-hidden="true" tabindex="-1"></a>X_train, X_test, y_train, y_test <span class="op">=</span> X[:<span class="dv">60000</span>], X[<span class="dv">6000</span>:], y[:<span class="dv">60000</span>], y[<span class="dv">60000</span>:]</span></code></pre></div>
</div>
<div id="1be39152" class="cell markdown">
<p>We now conduct dimensionality reduction by principal component
analysis (PCA). This reduces the time to run the
OneVsRestClassifier/OneVsOneClassifier and even the SGD Classifier.</p>
</div>
<div id="d44f891c" class="cell code" data-execution_count="18">
<div class="sourceCode" id="cb17"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1"></a>pca <span class="op">=</span> PCA(n_components <span class="op">=</span> <span class="fl">0.95</span>)</span>
<span id="cb17-2"><a href="#cb17-2" aria-hidden="true" tabindex="-1"></a>X_pca <span class="op">=</span> pca.fit_transform(X_train)</span></code></pre></div>
</div>
<div id="2b1aa91e" class="cell code" data-execution_count="21"
data-scrolled="true">
<div class="sourceCode" id="cb18"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb18-1"><a href="#cb18-1" aria-hidden="true" tabindex="-1"></a>X_pca.shape <span class="co">#This only has 154 y-coordinates as opposed to 784</span></span></code></pre></div>
<div class="output execute_result" data-execution_count="21">
<pre><code>(60000, 154)</code></pre>
</div>
</div>
<div id="f459e73b" class="cell markdown">
<p>Let us see what dimensionality reduction has done to X[0] (we
identified it earlier as 5). We use inverse_transform.</p>
</div>
<div id="f50d9b1b" class="cell code" data-execution_count="28">
<div class="sourceCode" id="cb20"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb20-1"><a href="#cb20-1" aria-hidden="true" tabindex="-1"></a>X_inv_pca <span class="op">=</span> pca.inverse_transform(X_pca)</span></code></pre></div>
</div>
<div id="564c226c" class="cell markdown">
<p>The X_inv_pca[0] is still 5 and dimensionality reduction has not
affected it, as we see next.</p>
</div>
<div id="5b08e08c" class="cell code" data-execution_count="29"
data-scrolled="true">
<div class="sourceCode" id="cb21"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb21-1"><a href="#cb21-1" aria-hidden="true" tabindex="-1"></a>same_digit <span class="op">=</span> X_inv_pca[<span class="dv">0</span>]</span>
<span id="cb21-2"><a href="#cb21-2" aria-hidden="true" tabindex="-1"></a>same_digit_image <span class="op">=</span> same_digit.reshape(<span class="dv">28</span>,<span class="dv">28</span>)</span>
<span id="cb21-3"><a href="#cb21-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb21-4"><a href="#cb21-4" aria-hidden="true" tabindex="-1"></a>plt.imshow(same_digit_image, cmap<span class="op">=</span> <span class="st">&quot;binary&quot;</span>)</span>
<span id="cb21-5"><a href="#cb21-5" aria-hidden="true" tabindex="-1"></a>plt.axis(<span class="st">&quot;off&quot;</span>)</span>
<span id="cb21-6"><a href="#cb21-6" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img src="f616f367c0186022e5c30fd293a5fbede59bc723.png" /></p>
</div>
</div>
<div id="f850b0ac" class="cell markdown">
<p>However, to make sure that PCA reduction has not distorted our image
of 5 in X[0] significantly.</p>
</div>
<div id="dd5b9cb7" class="cell code">
<div class="sourceCode" id="cb22"><pre
class="sourceCode python"><code class="sourceCode python"></code></pre></div>
</div>
<div id="3a3b32a3" class="cell markdown">
<p>First we employ a support a support vector machine in conjunction
with Principal Component Analysis dimensionality reduction.</p>
</div>
<div id="2227877b" class="cell code" data-execution_count="34">
<div class="sourceCode" id="cb23"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb23-1"><a href="#cb23-1" aria-hidden="true" tabindex="-1"></a>svm <span class="op">=</span>  SVC()</span>
<span id="cb23-2"><a href="#cb23-2" aria-hidden="true" tabindex="-1"></a>t_0 <span class="op">=</span> time.time()</span>
<span id="cb23-3"><a href="#cb23-3" aria-hidden="true" tabindex="-1"></a>svm.fit(X_pca, y_train)</span>
<span id="cb23-4"><a href="#cb23-4" aria-hidden="true" tabindex="-1"></a>t_1 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="dda0713b" class="cell code" data-execution_count="35">
<div class="sourceCode" id="cb24"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb24-1"><a href="#cb24-1" aria-hidden="true" tabindex="-1"></a>svm_training_time <span class="op">=</span> t_1<span class="op">-</span> t_0</span>
<span id="cb24-2"><a href="#cb24-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(svm_training_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>129.54357981681824
</code></pre>
</div>
</div>
<div id="d8ffe203" class="cell code" data-execution_count="37">
<div class="sourceCode" id="cb26"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb26-1"><a href="#cb26-1" aria-hidden="true" tabindex="-1"></a>svm.predict([X_pca[<span class="dv">0</span>]]) <span class="co">#does correctly identify it as 5</span></span></code></pre></div>
<div class="output execute_result" data-execution_count="37">
<pre><code>array([5], dtype=uint8)</code></pre>
</div>
</div>
<div id="2a25b616" class="cell code" data-execution_count="40">
<div class="sourceCode" id="cb28"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb28-1"><a href="#cb28-1" aria-hidden="true" tabindex="-1"></a>cross_val_score(svm, X_pca, y_train, cv<span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>) <span class="co">#it shows accuracy of roughly 98%!</span></span></code></pre></div>
<div class="output execute_result" data-execution_count="40">
<pre><code>array([0.98045, 0.97745, 0.97885])</code></pre>
</div>
</div>
<div id="2fdbde63" class="cell code">
<div class="sourceCode" id="cb30"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb30-1"><a href="#cb30-1" aria-hidden="true" tabindex="-1"></a>We employ the OneVsRestClassifier.</span>
<span id="cb30-2"><a href="#cb30-2" aria-hidden="true" tabindex="-1"></a></span></code></pre></div>
</div>
<div id="c21d017b" class="cell code" data-execution_count="44">
<div class="sourceCode" id="cb31"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb31-1"><a href="#cb31-1" aria-hidden="true" tabindex="-1"></a>ovr <span class="op">=</span> OneVsRestClassifier(SVC())</span>
<span id="cb31-2"><a href="#cb31-2" aria-hidden="true" tabindex="-1"></a>t_3<span class="op">=</span> time.time()</span>
<span id="cb31-3"><a href="#cb31-3" aria-hidden="true" tabindex="-1"></a>ovr.fit(X_pca, y_train)</span>
<span id="cb31-4"><a href="#cb31-4" aria-hidden="true" tabindex="-1"></a>t_4 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="cf9a8cf7" class="cell code" data-execution_count="45">
<div class="sourceCode" id="cb32"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb32-1"><a href="#cb32-1" aria-hidden="true" tabindex="-1"></a>ovr_training_time <span class="op">=</span> t_4<span class="op">-</span>t_3</span>
<span id="cb32-2"><a href="#cb32-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(ovr_training_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>648.283209323883
</code></pre>
</div>
</div>
<div id="0194a843" class="cell code">
<div class="sourceCode" id="cb34"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb34-1"><a href="#cb34-1" aria-hidden="true" tabindex="-1"></a>t_5 <span class="op">=</span>time.time()</span>
<span id="cb34-2"><a href="#cb34-2" aria-hidden="true" tabindex="-1"></a>cross_val_score(ovr, X_pca, y_train, cv<span class="op">=</span><span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>)</span>
<span id="cb34-3"><a href="#cb34-3" aria-hidden="true" tabindex="-1"></a>t_6 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="02e04145" class="cell code">
<div class="sourceCode" id="cb35"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb35-1"><a href="#cb35-1" aria-hidden="true" tabindex="-1"></a>cross_val_ovr_training_time <span class="op">=</span> t_6<span class="op">-</span>t_5</span>
<span id="cb35-2"><a href="#cb35-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_ovr_training_time)</span></code></pre></div>
</div>
<div id="57f357e6" class="cell markdown">
<p>The OneVsRestClassifier takes 648 seconds to train! We this resort to
Incremental PCA, where we divide the MNIST dataset into 100 batches and
use incremental PCA to reduce the dimension to 154 as before.</p>
</div>
<div id="44a28176" class="cell code" data-execution_count="65">
<div class="sourceCode" id="cb36"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb36-1"><a href="#cb36-1" aria-hidden="true" tabindex="-1"></a>n_batches <span class="op">=</span> <span class="dv">100</span></span>
<span id="cb36-2"><a href="#cb36-2" aria-hidden="true" tabindex="-1"></a>ipca <span class="op">=</span> IncrementalPCA(n_components <span class="op">=</span> <span class="dv">154</span>)</span>
<span id="cb36-3"><a href="#cb36-3" aria-hidden="true" tabindex="-1"></a>t_7 <span class="op">=</span> time.time()</span>
<span id="cb36-4"><a href="#cb36-4" aria-hidden="true" tabindex="-1"></a><span class="cf">for</span> train_batch <span class="kw">in</span> np.array_split(X_train, n_batches):</span>
<span id="cb36-5"><a href="#cb36-5" aria-hidden="true" tabindex="-1"></a>    ipca.partial_fit(train_batch)</span>
<span id="cb36-6"><a href="#cb36-6" aria-hidden="true" tabindex="-1"></a>    </span>
<span id="cb36-7"><a href="#cb36-7" aria-hidden="true" tabindex="-1"></a>X_ipca <span class="op">=</span> ipca.transform(X_train)</span>
<span id="cb36-8"><a href="#cb36-8" aria-hidden="true" tabindex="-1"></a>t_8 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="b1d0c8e3" class="cell code" data-execution_count="66">
<div class="sourceCode" id="cb37"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb37-1"><a href="#cb37-1" aria-hidden="true" tabindex="-1"></a>incremental_pca_training_time <span class="op">=</span> t_8 <span class="op">-</span> t_7</span>
<span id="cb37-2"><a href="#cb37-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(incremental_pca_training_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>41.145543575286865
</code></pre>
</div>
</div>
<div id="75005cb6" class="cell code" data-execution_count="52">
<div class="sourceCode" id="cb39"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb39-1"><a href="#cb39-1" aria-hidden="true" tabindex="-1"></a>ovr_ipca <span class="op">=</span> OneVsRestClassifier(SVC())</span>
<span id="cb39-2"><a href="#cb39-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb39-3"><a href="#cb39-3" aria-hidden="true" tabindex="-1"></a>t_9<span class="op">=</span> time.time()</span>
<span id="cb39-4"><a href="#cb39-4" aria-hidden="true" tabindex="-1"></a>ovr_ipca.fit(X_ipca, y_train)</span>
<span id="cb39-5"><a href="#cb39-5" aria-hidden="true" tabindex="-1"></a>t_10 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="ce8e616a" class="cell code" data-execution_count="55">
<div class="sourceCode" id="cb40"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb40-1"><a href="#cb40-1" aria-hidden="true" tabindex="-1"></a>ovr_ipca_training_time <span class="op">=</span> t_10<span class="op">-</span>t_9</span>
<span id="cb40-2"><a href="#cb40-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(t_10<span class="op">-</span>t_9)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>653.1747479438782
</code></pre>
</div>
</div>
<div id="9122aa3d" class="cell code" data-execution_count="75">
<div class="sourceCode" id="cb42"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb42-1"><a href="#cb42-1" aria-hidden="true" tabindex="-1"></a>t_11 <span class="op">=</span> time.time()</span>
<span id="cb42-2"><a href="#cb42-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_score(ovr_ipca, X_ipca, y_train, cv <span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>))</span>
<span id="cb42-3"><a href="#cb42-3" aria-hidden="true" tabindex="-1"></a>t_12 <span class="op">=</span> time.time()</span></code></pre></div>
<div class="output stream stdout">
<pre><code>[0.98195 0.97855 0.97885]
</code></pre>
</div>
</div>
<div id="25c99354" class="cell code" data-execution_count="76">
<div class="sourceCode" id="cb44"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb44-1"><a href="#cb44-1" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(t_12<span class="op">-</span>t_11) <span class="co">#cross validation time required for ovr_ipca is about 1058 seconds!</span></span></code></pre></div>
<div class="output stream stdout">
<pre><code>941.6955380439758
</code></pre>
</div>
</div>
<div id="d9b95a12" class="cell code" data-execution_count="63">
<div class="sourceCode" id="cb46"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb46-1"><a href="#cb46-1" aria-hidden="true" tabindex="-1"></a>X_ipca.shape</span></code></pre></div>
<div class="output execute_result" data-execution_count="63">
<pre><code>(60000, 154)</code></pre>
</div>
</div>
<div id="898e39be" class="cell markdown">
<p>Let's give the Stochastic Gradient Descent a try.</p>
</div>
<div id="25244b2f" class="cell code" data-execution_count="77">
<div class="sourceCode" id="cb48"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb48-1"><a href="#cb48-1" aria-hidden="true" tabindex="-1"></a>t_13 <span class="op">=</span> time.time()</span>
<span id="cb48-2"><a href="#cb48-2" aria-hidden="true" tabindex="-1"></a>sgd <span class="op">=</span> SGDClassifier(random_state <span class="op">=</span> <span class="dv">2</span>)</span>
<span id="cb48-3"><a href="#cb48-3" aria-hidden="true" tabindex="-1"></a>sgd.fit(X_ipca, y_train)</span>
<span id="cb48-4"><a href="#cb48-4" aria-hidden="true" tabindex="-1"></a>t_14 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="ea6b4087" class="cell code" data-execution_count="79">
<div class="sourceCode" id="cb49"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb49-1"><a href="#cb49-1" aria-hidden="true" tabindex="-1"></a>sgd_time <span class="op">=</span> t_14<span class="op">-</span>t_13</span>
<span id="cb49-2"><a href="#cb49-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(sgd_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>38.12362289428711
</code></pre>
</div>
</div>
<div id="478a6972" class="cell code" data-execution_count="82">
<div class="sourceCode" id="cb51"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb51-1"><a href="#cb51-1" aria-hidden="true" tabindex="-1"></a>t_15 <span class="op">=</span> time.time()</span>
<span id="cb51-2"><a href="#cb51-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_score(sgd, X_ipca, y_train, cv <span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>))</span>
<span id="cb51-3"><a href="#cb51-3" aria-hidden="true" tabindex="-1"></a>t_16 <span class="op">=</span> time.time()</span></code></pre></div>
<div class="output stream stdout">
<pre><code>[0.88265 0.8813  0.89215]
</code></pre>
</div>
</div>
<div id="9b82f22c" class="cell code" data-execution_count="84">
<div class="sourceCode" id="cb53"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb53-1"><a href="#cb53-1" aria-hidden="true" tabindex="-1"></a>cross_validation_time_sgd <span class="op">=</span> t_16<span class="op">-</span>t_15</span>
<span id="cb53-2"><a href="#cb53-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_validation_time_sgd)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>76.17458653450012
</code></pre>
</div>
</div>
<div id="084296b5" class="cell markdown">
<p>Just for the sake of completeness, let us now use the svm on
X_ipac.</p>
</div>
<div id="f2a0a9f4" class="cell code" data-execution_count="92">
<div class="sourceCode" id="cb55"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb55-1"><a href="#cb55-1" aria-hidden="true" tabindex="-1"></a>svm_ipca <span class="op">=</span>  SVC()</span>
<span id="cb55-2"><a href="#cb55-2" aria-hidden="true" tabindex="-1"></a>t_17 <span class="op">=</span> time.time()</span>
<span id="cb55-3"><a href="#cb55-3" aria-hidden="true" tabindex="-1"></a>svm_ipca.fit(X_ipca, y_train)</span>
<span id="cb55-4"><a href="#cb55-4" aria-hidden="true" tabindex="-1"></a>t_18 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="04bb9293" class="cell code" data-execution_count="93">
<div class="sourceCode" id="cb56"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb56-1"><a href="#cb56-1" aria-hidden="true" tabindex="-1"></a>svm_ipca_train_time <span class="op">=</span> t_18<span class="op">-</span>t_17</span>
<span id="cb56-2"><a href="#cb56-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(svm_ipca_train_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>150.82299041748047
</code></pre>
</div>
</div>
<div id="33ae82c2" class="cell code" data-execution_count="94">
<div class="sourceCode" id="cb58"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb58-1"><a href="#cb58-1" aria-hidden="true" tabindex="-1"></a>t_19 <span class="op">=</span> time.time()</span>
<span id="cb58-2"><a href="#cb58-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_score(svm_ipca, X_ipca, y_train, cv <span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>))</span>
<span id="cb58-3"><a href="#cb58-3" aria-hidden="true" tabindex="-1"></a>t_20 <span class="op">=</span> time.time()</span></code></pre></div>
<div class="output stream stdout">
<pre><code>[0.98045 0.9777  0.9791 ]
</code></pre>
</div>
</div>
<div id="086a3aba" class="cell code" data-execution_count="95">
<div class="sourceCode" id="cb60"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb60-1"><a href="#cb60-1" aria-hidden="true" tabindex="-1"></a>t_20<span class="op">-</span>t_19 <span class="co">#time for cross validation cvm_ipca</span></span></code></pre></div>
<div class="output execute_result" data-execution_count="95">
<pre><code>486.25614857673645</code></pre>
</div>
</div>
<div id="cf991658" class="cell markdown">
<p>Random Forest Regressor</p>
</div>
<div id="0a1fabd4" class="cell code" data-execution_count="99">
<div class="sourceCode" id="cb62"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb62-1"><a href="#cb62-1" aria-hidden="true" tabindex="-1"></a>rf <span class="op">=</span> RandomForestClassifier(n_estimators <span class="op">=</span> <span class="dv">100</span>)</span>
<span id="cb62-2"><a href="#cb62-2" aria-hidden="true" tabindex="-1"></a>t_21 <span class="op">=</span> time.time()</span>
<span id="cb62-3"><a href="#cb62-3" aria-hidden="true" tabindex="-1"></a>rf.fit(X_ipca, y_train)</span>
<span id="cb62-4"><a href="#cb62-4" aria-hidden="true" tabindex="-1"></a>t_22 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="5ace91cb" class="cell code" data-execution_count="100">
<div class="sourceCode" id="cb63"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb63-1"><a href="#cb63-1" aria-hidden="true" tabindex="-1"></a>rf_train_time <span class="op">=</span> t_22<span class="op">-</span>t_21</span>
<span id="cb63-2"><a href="#cb63-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(rf_train_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>146.90779566764832
</code></pre>
</div>
</div>
<div id="930cd69c" class="cell code" data-execution_count="101">
<div class="sourceCode" id="cb65"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb65-1"><a href="#cb65-1" aria-hidden="true" tabindex="-1"></a>t_23 <span class="op">=</span> time.time()</span>
<span id="cb65-2"><a href="#cb65-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_score(rf, X_ipca, y_train, cv<span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>))</span>
<span id="cb65-3"><a href="#cb65-3" aria-hidden="true" tabindex="-1"></a>t_24<span class="op">=</span> time.time()</span></code></pre></div>
<div class="output stream stdout">
<pre><code>[0.94115 0.93775 0.9445 ]
</code></pre>
</div>
</div>
<div id="5c587b68" class="cell code" data-execution_count="102">
<div class="sourceCode" id="cb67"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb67-1"><a href="#cb67-1" aria-hidden="true" tabindex="-1"></a>t_24<span class="op">-</span>t_23 <span class="co">#cross validation time for random forest</span></span></code></pre></div>
<div class="output execute_result" data-execution_count="102">
<pre><code>250.1513705253601</code></pre>
</div>
</div>
<div id="31ac67b5" class="cell markdown">
<p>Let's just work with the Random Forest Classifier with just the
X_pca</p>
</div>
<div id="ade5b590" class="cell code" data-execution_count="104">
<div class="sourceCode" id="cb69"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb69-1"><a href="#cb69-1" aria-hidden="true" tabindex="-1"></a>rf2 <span class="op">=</span> RandomForestClassifier(n_estimators <span class="op">=</span> <span class="dv">100</span>)</span>
<span id="cb69-2"><a href="#cb69-2" aria-hidden="true" tabindex="-1"></a>t_25 <span class="op">=</span> time.time()</span>
<span id="cb69-3"><a href="#cb69-3" aria-hidden="true" tabindex="-1"></a>rf2.fit(X_pca, y_train)</span>
<span id="cb69-4"><a href="#cb69-4" aria-hidden="true" tabindex="-1"></a>t_26<span class="op">=</span>time.time()</span></code></pre></div>
</div>
<div id="1a839a5e" class="cell code" data-execution_count="105">
<div class="sourceCode" id="cb70"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb70-1"><a href="#cb70-1" aria-hidden="true" tabindex="-1"></a>rf2_train_time <span class="op">=</span> t_26<span class="op">-</span>t_25</span>
<span id="cb70-2"><a href="#cb70-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(rf2_train_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>141.91917967796326
</code></pre>
</div>
</div>
<div id="2a66d3c4" class="cell code" data-execution_count="106">
<div class="sourceCode" id="cb72"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb72-1"><a href="#cb72-1" aria-hidden="true" tabindex="-1"></a>t_27 <span class="op">=</span> time.time()</span>
<span id="cb72-2"><a href="#cb72-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_score(rf, X_pca, y_train, cv<span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>))</span>
<span id="cb72-3"><a href="#cb72-3" aria-hidden="true" tabindex="-1"></a>t_28<span class="op">=</span> time.time()</span></code></pre></div>
<div class="output stream stdout">
<pre><code>[0.9412 0.9372 0.9434]
</code></pre>
</div>
</div>
<div id="0f4eb90c" class="cell code" data-execution_count="107">
<div class="sourceCode" id="cb74"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb74-1"><a href="#cb74-1" aria-hidden="true" tabindex="-1"></a>t_28<span class="op">-</span>t_27</span></code></pre></div>
<div class="output execute_result" data-execution_count="107">
<pre><code>310.8674564361572</code></pre>
</div>
</div>
<div id="81f986a4" class="cell markdown">
<p>And finally, just to satisfy our curiosity, we run a random forest
classifier naively on X_train without dimensionality reduction</p>
</div>
<div id="77d768b1" class="cell code" data-execution_count="109">
<div class="sourceCode" id="cb76"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb76-1"><a href="#cb76-1" aria-hidden="true" tabindex="-1"></a>rf3 <span class="op">=</span> RandomForestClassifier(n_estimators <span class="op">=</span> <span class="dv">100</span>)</span>
<span id="cb76-2"><a href="#cb76-2" aria-hidden="true" tabindex="-1"></a>t_29 <span class="op">=</span> time.time()</span>
<span id="cb76-3"><a href="#cb76-3" aria-hidden="true" tabindex="-1"></a>rf3.fit(X_train, y_train)</span>
<span id="cb76-4"><a href="#cb76-4" aria-hidden="true" tabindex="-1"></a>t_30 <span class="op">=</span> time.time()</span></code></pre></div>
</div>
<div id="a55bde3a" class="cell code" data-execution_count="110">
<div class="sourceCode" id="cb77"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb77-1"><a href="#cb77-1" aria-hidden="true" tabindex="-1"></a>rf3_train_time <span class="op">=</span> t_30<span class="op">-</span>t_29</span>
<span id="cb77-2"><a href="#cb77-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(rf3_train_time)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>55.75401329994202
</code></pre>
</div>
</div>
<div id="9e004ed8" class="cell code" data-execution_count="111">
<div class="sourceCode" id="cb79"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb79-1"><a href="#cb79-1" aria-hidden="true" tabindex="-1"></a>t_31 <span class="op">=</span> time.time()</span>
<span id="cb79-2"><a href="#cb79-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(cross_val_score(rf3, X_train, y_train, cv<span class="op">=</span> <span class="dv">3</span>, scoring <span class="op">=</span> <span class="st">&quot;accuracy&quot;</span>))</span>
<span id="cb79-3"><a href="#cb79-3" aria-hidden="true" tabindex="-1"></a>t_32<span class="op">=</span> time.time()</span></code></pre></div>
<div class="output stream stdout">
<pre><code>[0.9657  0.96225 0.96625]
</code></pre>
</div>
</div>
<div id="81ea6305" class="cell code" data-execution_count="112">
<div class="sourceCode" id="cb81"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb81-1"><a href="#cb81-1" aria-hidden="true" tabindex="-1"></a>t_32<span class="op">-</span>t_31 <span class="co">#cross validation time for random forest without pca reduction on X_train</span></span></code></pre></div>
<div class="output execute_result" data-execution_count="112">
<pre><code>123.347585439682</code></pre>
</div>
</div>
<div id="5e596094" class="cell code">
<div class="sourceCode" id="cb83"><pre
class="sourceCode python"><code class="sourceCode python"></code></pre></div>
</div>
</body>
</html>
