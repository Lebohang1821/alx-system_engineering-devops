# It installs flask from pip3, Using Puppe
package { 'flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3',
}
