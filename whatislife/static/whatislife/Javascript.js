function submitButton(me)
{
  /*var value = me.parentNode.querySelector('input').value;*/
    var newCol = me.parentNode.querySelector('input').value;
    console.log(newCol);
//   document.getElementById('text_box').style.color = newCol;
  var elements = document.getElementsByClassName('text_box');
for (var i = 0, len = elements.length; i<len; i++)
  {
    elements[i].style['color'] = newCol;
  }
}

// var form = document.createElement('form');
// var p = document.createElement('p');
// p.textContent = 'What color would you like the font on this page?';
// form.appendChild(p);

// var input = document.createElement('input');
// input.type = 'text';
// input.name = 'colorinput';
// form.appendChild(input);

// /*<button type = 'button' onclick=tribButton(this)>*/
// var button = document.createElement('button');
// button.type='button';
// button.onclick = submitButton(this);
// form.appendChild(button);
// /*document.querySelector('body').appendChild(linkListDiv);*/

// document.querySelector('body').appendChild(form);
